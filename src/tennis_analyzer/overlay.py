import logging

import cv2

logger = logging.getLogger(__name__)

from tennis_analyzer.config import (
    BODY_COLOR,
    PART_NOSE,
    PARTS_ARM,
    PARTS_BODY,
    SPIN_COLOR,
)


def get_body_point(body_part, height, width):
    body_point = (
        int(body_part[0] * width),
        int(body_part[1] * height),
    )

    return body_point


def get_all_body_points(body_parts, coordinates, height, width, dominant_hand=None):
    if dominant_hand:
        all_body_points = {
            part: get_body_point(coordinates[f"{part}_{dominant_hand}"], height, width) for part in body_parts
        }
    else:
        all_body_points = {
            part: get_body_point(coordinates["nose"], height, width) for part in body_parts
        }

    return all_body_points


def put_text(coordinates, spin, frame):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    points = get_all_body_points(PART_NOSE, coordinates, height, width)

    for part in PART_NOSE:
        frame = cv2.putText(
            frame,
            spin,
            (points[part][0] - 40, points[part][1] - 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            SPIN_COLOR[spin],
            2,
        )

    return frame


def draw_lines(coordinates, frame, spin, dominant_hand, body_color_select=False):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    if body_color_select:
        body_color = BODY_COLOR
    else:
        body_color = SPIN_COLOR[spin]

    height, width = frame.shape[:2]

    points_body = get_all_body_points(PARTS_BODY, coordinates, height, width, dominant_hand)

    for parts in zip(PARTS_BODY, PARTS_BODY[1:]):
        cv2.line(frame, points_body[parts[0]], points_body[parts[1]], body_color, 2)

    points_arm = get_all_body_points(PARTS_ARM, coordinates, height, width, dominant_hand)

    for parts in zip(PARTS_ARM, PARTS_ARM[1:]):
        cv2.line(frame, points_arm[parts[0]], points_arm[parts[1]], SPIN_COLOR[spin], 2)

    return frame


def annotate_frame(spin, frame, coordinates, dominant_hand, body_color_select):
    frame = put_text(coordinates, spin, frame)
    frame = draw_lines(coordinates, frame, spin, dominant_hand, body_color_select)

    return frame
