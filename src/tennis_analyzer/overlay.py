import logging

import cv2

logger = logging.getLogger(__name__)

from tennis_analyzer.config import (
    BODY_COLOR,
    PART_NOSE,
    PARTS_ARM,
    PARTS_BODY,
    SEPARATE_BODY_COLOR,
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
            part: get_body_point(coordinates[f"{part}_{dominant_hand}"], height, width)
            for part in body_parts
        }
    else:
        all_body_points = {
            part: get_body_point(coordinates["nose"], height, width)
            for part in body_parts
        }

    return all_body_points


def create_lines(frame, body_parts, points, color):
    for parts in zip(body_parts, body_parts[1:]):
        cv2.line(frame, points[parts[0]], points[parts[1]], color, 2)


def put_text(coordinates, spin, frame):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    height, width = frame.shape[:2]

    points = get_all_body_points(PART_NOSE, coordinates, height, width)

    for part in PART_NOSE:
        frame = cv2.putText(
            frame,
            spin.value,
            (points[part][0] - 40, points[part][1] - 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            SPIN_COLOR[spin],
            2,
        )

    return frame


def draw_body_lines(
    frame, body_parts, coordinates, height, width, dominant_hand, color
):
    points = get_all_body_points(body_parts, coordinates, height, width, dominant_hand)
    create_lines(frame, body_parts, points, color)


def draw_lines(coordinates, frame, spin, dominant_hand):
    if frame is None:
        logger.warning("Frame is None, skipping overlay.")
        return None

    if SEPARATE_BODY_COLOR:
        body_color = BODY_COLOR
    else:
        body_color = SPIN_COLOR[spin]

    height, width = frame.shape[:2]

    draw_body_lines(
        frame, PARTS_BODY, coordinates, height, width, dominant_hand, body_color
    )

    draw_body_lines(
        frame, PARTS_ARM, coordinates, height, width, dominant_hand, SPIN_COLOR[spin]
    )

    return frame


def annotate_frame(spin, frame, coordinates, dominant_hand):
    frame = put_text(coordinates, spin, frame)
    frame = draw_lines(coordinates, frame, spin, dominant_hand)

    return frame
