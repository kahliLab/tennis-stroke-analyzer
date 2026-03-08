import cv2


def load_video(path):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        raise ValueError(f"Video {path} konnte nicht geöffnet werden.")

    return cap

def extract_frames(cap):
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    return frames
