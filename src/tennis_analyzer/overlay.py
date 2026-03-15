import cv2

STROKE_COLOUR = {"Topspin": (0, 0, 255), "Flat": (0, 255, 0), "Slice": (255, 0, 0)}


def put_text(stroke, frame):
    frame_with_text = cv2.putText(
        frame, stroke, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, STROKE_COLOUR[stroke], 2
    )

    return frame_with_text


def draw_lines(coordindates, frame, stroke, dominant_hand):
    height, width = frame.shape[:2]

    shoulder = coordindates[f"shoulder_{dominant_hand}"]
    elbow = coordindates[f"elbow_{dominant_hand}"]
    wrist = coordindates[f"wrist_{dominant_hand}"]

    get_point = lambda body_part: (
        int(body_part[0] * width),
        int(body_part[1] * height),
    )

    point_shoulder = get_point(shoulder)
    point_elbow = get_point(elbow)
    point_wrist = get_point(wrist)

    cv2.line(frame, point_shoulder, point_elbow, STROKE_COLOUR[stroke], 2)
    cv2.line(frame, point_elbow, point_wrist, STROKE_COLOUR[stroke], 2)

    return frame
