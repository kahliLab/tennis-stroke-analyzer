from video_processor import load_video, extract_frames, export_video
from pose_tracker import get_pose_data, get_landmarks, get_coordinates, init_pose
from stroke_classifier import classify_stroke, detect_dominant_hand
from overlay import put_text, draw_lines

def main():
    #video = some Path
    cap, fps = load_video(video)
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


if __name__ == "__main__":
    main()