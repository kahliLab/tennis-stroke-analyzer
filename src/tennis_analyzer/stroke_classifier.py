import logging

logger = logging.getLogger(__name__)

from tennis_analyzer.config import THRESHOLD


def detect_dominant_hand(pose_data, lefty=False):
    dominant_hand = None

    if not pose_data:
        logger.error("No pose data available.")
        raise ValueError("Detecting dominant is not possible without pose data.")

    left_hand = [i["wrist_left"][1] for i in pose_data if i.get("wrist_left")]
    right_hand = [i["wrist_right"][1] for i in pose_data if i.get("wrist_right")]

    get_diff = lambda diff: sum(abs(a - b) for a, b in zip(diff[1:], diff[:-1]))

    left_diff, right_diff = get_diff(left_hand), get_diff(right_hand)

    if left_diff > right_diff:
        dominant_hand = "left"
    else:
        dominant_hand = "right"

    if lefty:
        dominant_hand = "left"

    logger.info(f"Dominant hand is {dominant_hand}")

    return dominant_hand


def classify_stroke(pose_data):
    dominant_hand = f"_{detect_dominant_hand(pose_data)}"

    start_pose, end_pose = pose_data[0], pose_data[-1]

    get_y = lambda pose, part: pose[f"{part}{dominant_hand}"][1]

    wrist_start = get_y(start_pose, "wrist")
    wrist_end = get_y(end_pose, "wrist")
    elbow_start = get_y(start_pose, "elbow")
    elbow_end = get_y(end_pose, "elbow")

    if abs(wrist_start - elbow_start) < THRESHOLD:
        stroke = "Flat"
    elif wrist_start < elbow_start and wrist_end > elbow_end:
        stroke = "Slice"
    elif wrist_start > elbow_start and wrist_end < elbow_end:
        stroke = "Topspin"
    else:
        stroke = "Learn tennis first!"

    if stroke == "Learn tennis first!":
        logger.warning("That's one weird stroke you have there...")
    else:
        logger.info(f"Stroke in frame classified as {stroke.lower()}")

    return stroke
