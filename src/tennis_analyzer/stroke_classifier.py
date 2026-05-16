import logging

logger = logging.getLogger(__name__)

from tennis_analyzer.config import LEFTY, THRESHOLD, Spin


def calculate_total_movement(hand):
    total_movement = sum(abs(a - b) for a, b in zip(hand[1:], hand[:-1]))

    return total_movement


def detect_dominant_hand(pose_data):
    if not pose_data:
        logger.error("No pose data available.")
        raise ValueError("Detecting dominant is not possible without pose data.")

    if LEFTY:
        dominant_hand = "left"
        return dominant_hand

    left_hand = [i["wrist_left"][1] for i in pose_data if i.get("wrist_left")]
    right_hand = [i["wrist_right"][1] for i in pose_data if i.get("wrist_right")]

    left_diff = calculate_total_movement(left_hand)
    right_diff = calculate_total_movement(right_hand)

    if left_diff > right_diff:
        dominant_hand = "left"
    else:
        dominant_hand = "right"

    logger.info(f"Dominant hand is {dominant_hand}")

    return dominant_hand


def get_y_coordinate(pose, part, dominant_hand_suffix):
    y_coordinate = pose[f"{part}{dominant_hand_suffix}"][1]

    return y_coordinate


def classify_spin(pose_data, dominant_hand):
    dominant_hand_suffix = f"_{dominant_hand}"

    start_pose, end_pose = pose_data[0], pose_data[-1]

    wrist_start = get_y_coordinate(start_pose, "wrist", dominant_hand_suffix)
    wrist_end = get_y_coordinate(end_pose, "wrist", dominant_hand_suffix)
    elbow_start = get_y_coordinate(start_pose, "elbow", dominant_hand_suffix)
    elbow_end = get_y_coordinate(end_pose, "elbow", dominant_hand_suffix)

    if abs(wrist_start - elbow_start) < THRESHOLD:
        spin = Spin.FLAT
    elif wrist_start < elbow_start and wrist_end > elbow_end:
        spin = Spin.SLICE
    elif wrist_start > elbow_start and wrist_end < elbow_end:
        spin = Spin.TOPSPIN
    else:
        spin = Spin.LEARN_TENNIS

    if spin == Spin.LEARN_TENNIS:
        logger.warning("That's one weird spin you have there...")
    else:
        logger.info(f"spin in frame classified as {spin.value.lower()}")

    return spin
