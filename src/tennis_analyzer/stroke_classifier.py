THRESHOLD = 0.05


def detect_dominant_hand(pose_data):
    dominant_hand = None

    left_hand = [
        i["handgelenk_links"][1] for i in pose_data if i.get("handgelenk_links")
    ]
    right_hand = [
        i["handgelenk_rechts"][1] for i in pose_data if i.get("handgelenk_rechts")
    ]

    get_diff = lambda diff: sum(abs(a - b) for a, b in zip(diff[1:], diff[:-1]))

    left_diff = get_diff(left_hand)
    right_diff = get_diff(right_hand)

    if left_diff > right_diff:
        dominant_hand = "left"
    else:
        dominant_hand = "right"

    return dominant_hand


def classify_stroke(pose_data):
    dominant_hand = detect_dominant_hand(pose_data)

    if dominant_hand == "left":
        select_hand = "_links"
    else:
        select_hand = "_rechts"

    start_pose, end_pose = pose_data[0], pose_data[-1]

    get_y = lambda pose, part: pose[f"{part}{select_hand}"][1]

    handgelenk_start = get_y(start_pose, "handgelenk")
    handgelenk_end = get_y(end_pose, "handgelenk")
    ellbogen_start = get_y(start_pose, "ellbogen")
    ellbogen_end = get_y(end_pose, "ellbogen")

    if abs(handgelenk_start - ellbogen_start) < THRESHOLD:
        stroke = "Flat"
    elif handgelenk_start < ellbogen_start and handgelenk_end > ellbogen_end:
        stroke = "Topspin"
    elif handgelenk_start > ellbogen_start and handgelenk_end < ellbogen_end:
        stroke = "Slice"
    else:
        stroke = "Learn tennis first!"

    return stroke
