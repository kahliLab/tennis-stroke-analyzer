import cv2
import mediapipe as mp
import logging

logger = logging.getLogger(__name__)

def init_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    logger.info("Pose initialized.")

    return pose


def get_landmarks(frame, pose):
    fixed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    landmarks = pose.process(fixed_frame)

    if not landmarks.pose_landmarks:
        logger.warning("No landmarks found in frame.")
        return None

    return landmarks.pose_landmarks


def get_coordinates(landmarks):
    coordinates_from_landmark = lambda landmark: [landmark.x, landmark.y, landmark.z]

    body_parts_index = {
        "shoulder_left": 11,
        "shoulder_right": 12,
        "elbow_left": 13,
        "elbow_right": 14,
        "wrist_left": 15,
        "wrist_right": 16,
    }

    coordinates = {
        key: coordinates_from_landmark(landmarks.landmark[value])
        for key, value in body_parts_index.items()
    }

    if not coordinates:
        logger.error("No coordinates found!")
        raise ValueError("Failed to extract coordinates from landmarks!")

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

    logger.info(f"Processed {len(pose_data)} frames with landmarks out of {len(frames)} total.")
    return pose_data
