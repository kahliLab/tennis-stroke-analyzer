from enum import Enum

THRESHOLD = 0.05

# TODO Dominant hand is hard set via constant to override detection (which still needs some work)
LEFTY = True
SEPARATE_BODY_COLOR = False


class Spin(Enum):
    TOPSPIN = "Topspin"
    FLAT = "Flat"
    SLICE = "Slice"
    LEARN_TENNIS = "Learn tennis first!"


SPIN_COLOR = {
    Spin.TOPSPIN: (0, 0, 255),
    Spin.FLAT: (0, 255, 0),
    Spin.SLICE: (255, 0, 0),
    Spin.LEARN_TENNIS: (238, 130, 238),
}

BODY_COLOR = (0, 255, 255)

ALL_LANDMARKS = {
    "nose": 0,
    "left_eye_inner": 1,
    "left_eye": 2,
    "left_eye_outer": 3,
    "right_eye_inner": 4,
    "right_eye": 5,
    "right_eye_outer": 6,
    "left_ear": 7,
    "right_ear": 8,
    "mouth_left": 9,
    "mouth_right": 10,
    "shoulder_left": 11,
    "shoulder_right": 12,
    "elbow_left": 13,
    "elbow_right": 14,
    "wrist_left": 15,
    "wrist_right": 16,
    "pinky_left": 17,
    "pinky_right": 18,
    "index_left": 19,
    "index_right": 20,
    "thumb_left": 21,
    "thumb_right": 22,
    "hip_left": 23,
    "hip_right": 24,
    "knee_left": 25,
    "knee_right": 26,
    "ankle_left": 27,
    "ankle_right": 28,
    "heel_left": 29,
    "heel_right": 30,
    "foot_index_left": 31,
    "foot_index_right": 32,
}

PARTS = ["nose", "shoulder", "elbow", "wrist", "hip", "knee", "ankle", "foot_index"]
PART_NOSE = ["nose"]
PARTS_BODY = ["shoulder", "hip", "knee", "ankle", "foot_index"]
PARTS_ARM = ["shoulder", "elbow", "wrist"]

INPUT_PATH_VIDEO = "./data/input.mp4"
OUTPUT_PATH_VIDEO = "./output/output.mp4"
OUTPUT_PATH_GIF = "./output/output.gif"
