import mediapipe as mp


def init_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    return pose
