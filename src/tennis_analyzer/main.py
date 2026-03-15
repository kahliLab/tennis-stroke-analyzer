from overlay import draw_lines, put_text
from pose_tracker import get_coordinates, get_landmarks, get_pose_data, init_pose
from stroke_classifier import classify_stroke, detect_dominant_hand
from video_processor import export_video, extract_frames, load_video


def main():
    input_file = "./data/input.mp4"
    cap, fps = load_video(input_file)
    frames = extract_frames(cap)

    pose = init_pose()
    pose_data = get_pose_data(frames)

    dom_hand = detect_dominant_hand(pose_data)
    stroke = classify_stroke(pose_data)

    annotated_frames = []
    for frame in frames:
        landmarks = get_landmarks(frame, pose)
        coord = get_coordinates(landmarks)
        frame_with_text = put_text(stroke, frame)
        frame_with_text_and_lines = draw_lines(coord, frame_with_text, stroke, dom_hand)
        annotated_frames.append(frame_with_text_and_lines)

    output_file = export_video(fps, annotated_frames)


if __name__ == "__main__":
    main()
