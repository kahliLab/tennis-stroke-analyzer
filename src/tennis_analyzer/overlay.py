import logging
import cv2

logger = logging.getLogger(__name__)

from tennis_analyzer.config import STROKE_COLOUR, PARTS


def put_text(coordindates, stroke, frame):
    PART_NOSE = [p for p in PARTS if p == "nose"]
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    get_nose = lambda nose: (
        int(nose[0] * width),
        int(nose[1] * height),
    )

    points = {
        part: get_nose(coordindates["nose"]) for part in PART_NOSE
    }

    for part in PART_NOSE:
        frame = cv2.putText(
            frame, stroke, (points[part][0]-20, points[part][1]-40), cv2.FONT_HERSHEY_SIMPLEX, 1, STROKE_COLOUR[stroke], 2
        )

    return frame


def draw_lines(coordindates, frame, stroke, dominant_hand):
    PARTS_FOR_LINES = [p for p in PARTS if p != "nose"]
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    get_point = lambda body_part: (
        int(body_part[0] * width),
        int(body_part[1] * height),
    )

    points = {
        part: get_point(coordindates[f"{part}_{dominant_hand}"]) for part in PARTS_FOR_LINES
    }

    for parts in zip(PARTS_FOR_LINES, PARTS_FOR_LINES[1:]):
        cv2.line(frame, points[parts[0]], points[parts[1]], STROKE_COLOUR[stroke], 2)

    return frame


def annotate_frame(stroke, frame, coordinates, dominant_hand):
    frame = put_text(coordinates, stroke, frame)
    frame = draw_lines(coordinates, frame, stroke, dominant_hand)
    
    return frame
