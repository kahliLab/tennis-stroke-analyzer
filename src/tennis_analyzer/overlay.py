import logging
import cv2

logger = logging.getLogger(__name__)

from tennis_analyzer.config import STROKE_COLOUR, PARTS


def put_text(stroke, frame):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    frame = cv2.putText(
        frame, stroke, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, STROKE_COLOUR[stroke], 2
    )

    return frame


def draw_lines(coordindates, frame, stroke, dominant_hand):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    get_point = lambda body_part: (
        int(body_part[0] * width),
        int(body_part[1] * height),
    )

    points = {
        part: get_point(coordindates[f"{part}_{dominant_hand}"]) for part in PARTS
    }

    cv2.line(frame, points["shoulder"], points["elbow"], STROKE_COLOUR[stroke], 2)
    cv2.line(frame, points["elbow"], points["wrist"], STROKE_COLOUR[stroke], 2)

    return frame


def annotate_frame(stroke, frame, coordinates, dominant_hand):
    frame = put_text(stroke, frame)
    frame = draw_lines(coordinates, frame, stroke, frame, dominant_hand)
    
    return frame
