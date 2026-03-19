from tennis_analyzer.stroke_classifier import classify_stroke, detect_dominant_hand

x, y, z = 0.05

pose_data_topspin = [
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.13, z],
        "wrist_right": [x, 0.13, z],
    },
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
]

pose_data_slice = [
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.13, z],
        "wrist_right": [x, 0.13, z],
    },
]


pose_data_flat = [
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.10, z],
        "wrist_right": [x, 0.10, z],
    },
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.04, z],
        "wrist_right": [x, 0.04, z],
    },
]

pose_data_unknown = [
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.17, z],
        "elbow_right": [x, 0.17, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
    {
        "shoulder_left": [x, y, z],
        "shoulder_right": [x, y, z],
        "elbow_left": [x, 0.27, z],
        "elbow_right": [x, 0.27, z],
        "wrist_left": [x, 0.14, z],
        "wrist_right": [x, 0.14, z],
    },
]


def test_classifiy_stroke():
    stroke = classify_stroke(pose_data_topspin)
    assert stroke == "Topspin"
