import logging

import cv2
import imageio

from tennis_analyzer.config import OUTPUT_PATH_GIF, OUTPUT_PATH_VIDEO

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


def export_video(fps, frames, output_path=OUTPUT_PATH_VIDEO):
    height, width = frames[0].shape[:2]

    out = cv2.VideoWriter(
        output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()
    logger.info(f"MP4 export: Annotated frames successfully written to {output_path}!")


def export_gif(frames, output_path=OUTPUT_PATH_GIF):
    fixed_frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in frames]
    imageio.mimsave(output_path, fixed_frames, fps=30)

    logger.info(f"GIF export: Annotated frames successfully written to {output_path}!")
