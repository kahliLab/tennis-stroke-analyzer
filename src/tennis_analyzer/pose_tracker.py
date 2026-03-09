import mediapipe as mp
import cv2


def init_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    return pose


def get_landmarks(frame, pose):
    fixed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    landmarks = pose.process(fixed_frame)

    if not landmarks.pose_landmarks:
        return None

    return landmarks


def get_coordinates(landmarks):
    coordinates = lambda landmark: [landmark.x, landmark.y, landmark.z]

    body_parts_index = {
        "schulter_links": 11,
        "schulter_rechts": 12,
        "ellbogen_links": 13,
        "ellbogen_rechts": 14,
        "handgelenk_links": 15,
        "handgelenk_rechts": 16,
    }

    coordinates = {
        key: coordinates(landmarks.landmark[value])
        for key, value in body_parts_index.items()
    }

    return coordinates


def get_pose_data(frames):
    pose_data = []

    pose = init_pose()
    for frame in frames:
        landmarks = get_landmarks(frame, pose)
        if not landmarks:
            continue
        coordinates = get_coordinates(landmarks)
        pose_data.append(coordinates)

    return pose_data
