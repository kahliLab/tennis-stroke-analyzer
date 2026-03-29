import cv2
import mediapipe as mp
import logging

logger = logging.getLogger(__name__)

from tennis_analyzer.config import ALL_LANDMARKS, PARTS

def init_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    logger.info("Pose initialized.")

    return pose


def get_body_parts():
    body_parts = {}
    
    for part in PARTS:
        for key, value in ALL_LANDMARKS.items():
            if part in key:
                body_parts[key] = value

    return body_parts


def get_landmarks(frame, pose):
    fixed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    landmarks = pose.process(fixed_frame)

    if not landmarks.pose_landmarks:
        logger.warning("No landmarks found in frame.")
        return None

    return landmarks.pose_landmarks


def get_coordinates(body_parts, landmarks):
    coordinates_from_landmark = lambda landmark: [landmark.x, landmark.y, landmark.z]

    coordinates = {
        key: coordinates_from_landmark(landmarks.landmark[value])
        for key, value in body_parts.items()
    }

    if not coordinates:
        logger.error("No coordinates found!")
        raise ValueError("Failed to extract coordinates from landmarks!")

    return coordinates


def get_pose_data(frames):
    pose_data = []

    pose = init_pose()
    body_parts = get_body_parts()

    for frame in frames:
        landmarks = get_landmarks(frame, pose)
        if not landmarks:
            continue
        coordinates = get_coordinates(body_parts, landmarks)
        pose_data.append(coordinates)

    logger.info(f"Processed {len(pose_data)} frames with landmarks out of {len(frames)} total.")
    return pose_data
