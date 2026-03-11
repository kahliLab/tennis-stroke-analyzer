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
