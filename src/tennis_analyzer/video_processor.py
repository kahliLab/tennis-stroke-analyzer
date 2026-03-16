import cv2
import logging

logger = logging.getLogger(__name__)

def load_video(path):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        logger.error("Failed to open video source.")
        raise ValueError(f"Video {path} could not be opened.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    logger.info("Video loaded successfully!")

    return cap, fps


def extract_frames(cap):
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    logger.info(f"{len(frames)} frames extracted from video.")

    return frames


def export_video(fps, frames, output_path="./output/output.mp4"):
    height, width = frames[0].shape[:2]

    out = cv2.VideoWriter(
        output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()
    logger.info(f"Annotated frames successfully written to {output_path}!")

    return output_path
