import cv2

STROKE_COLOUR = {
    "topspin": (0, 0, 255),
    "flat": (0, 255, 0),
    "slice": (255, 0, 0)
}

def put_text(stroke, frame):
    frame_with_text = cv2.putText(
        frame,
        stroke,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        STROKE_COLOUR[stroke],
        2
    )

    return frame_with_text
