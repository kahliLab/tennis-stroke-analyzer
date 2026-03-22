import logging
import cv2

logger = logging.getLogger(__name__)

STROKE_COLOUR = {"Topspin": (0, 0, 255), "Flat": (0, 255, 0), "Slice": (255, 0, 0)}


def put_text(stroke, frame):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    frame_with_text = cv2.putText(
        frame, stroke, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, STROKE_COLOUR[stroke], 2
    )

    return frame_with_text


def draw_lines(coordindates, frame, stroke, dominant_hand):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    parts = ["shoulder", "elbow", "wrist"]

    get_point = lambda body_part: (
        int(body_part[0] * width),
        int(body_part[1] * height),
    )

    points = {
        part: get_point(coordindates[f"{part}_{dominant_hand}"]) for part in parts
    }

    cv2.line(frame, points["shoulder"], points["elbow"], STROKE_COLOUR[stroke], 2)
    cv2.line(frame, points["elbow"], points["wrist"], STROKE_COLOUR[stroke], 2)

    return frame
