import cv2


def load_video(path):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        raise ValueError(f"Video {path} konnte nicht geöffnet werden.")

    return cap
