import mediapipe as mp
import cv2


def init_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    return pose


def get_landmarks(frame, pose):
    fixed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = pose.process(fixed_frame)

    if not result.pose_landmarks:
        return None

    return result
