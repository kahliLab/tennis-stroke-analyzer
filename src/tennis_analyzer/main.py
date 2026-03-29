import logging

from tennis_analyzer.overlay import annotate_frame
from tennis_analyzer.pose_tracker import get_pose_data
from tennis_analyzer.stroke_classifier import classify_stroke, detect_dominant_hand
from tennis_analyzer.video_processor import export_video, export_gif, extract_frames, load_video
from tennis_analyzer.config import INPUT_PATH_VIDEO

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    try:
        input_file = INPUT_PATH_VIDEO
        cap, fps = load_video(input_file)
        frames = extract_frames(cap)

        pose_data = get_pose_data(frames)

        dom_hand = detect_dominant_hand(pose_data, lefty=True)
        stroke = classify_stroke(pose_data, dom_hand)

        annotated_frames = []
        for frame, coord in zip(frames, pose_data):
            annotated_frame = annotate_frame(stroke, frame, coord, dom_hand, body_color_select=False)
            annotated_frames.append(annotated_frame)

        export_video(fps, annotated_frames)
        export_gif(annotated_frames)

    except Exception as e:
        logger.error(f"Look here {e} for the error that crashed the programm.")


if __name__ == "__main__":
    main()
