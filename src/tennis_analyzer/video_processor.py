import cv2


def load_video(path):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        raise ValueError(f"Video {path} could not be opened.")

    fps = cap.get(cv2.CAP_PROP_FPS)

    return cap, fps


def extract_frames(cap):
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    return frames


def export_video(fps, frames, output_path="./output/output.mp4"):
    height, width = frames[0].shape[:2]

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()

    return output_path
