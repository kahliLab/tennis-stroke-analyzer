import pytest

from tennis_analyzer.config import LEFTY, Spin
from tennis_analyzer.stroke_classifier import classify_spin, detect_dominant_hand

x = y = z = 0.05

pose_data_topspin = [
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.13, z],
        "wrist_right": [x, 0.13, z],
    },
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
]

pose_data_slice = [
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.13, z],
        "wrist_right": [x, 0.13, z],
    },
]


pose_data_flat = [
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.10, z],
        "wrist_right": [x, 0.10, z],
    },
    {
        "elbow_left": [x, 0.07, z],
        "elbow_right": [x, 0.07, z],
        "wrist_left": [x, 0.04, z],
        "wrist_right": [x, 0.04, z],
    },
]

pose_data_unknown = [
    {
        "elbow_left": [x, 0.17, z],
        "elbow_right": [x, 0.17, z],
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.01, z],
    },
    {
        "elbow_left": [x, 0.27, z],
        "elbow_right": [x, 0.27, z],
        "wrist_left": [x, 0.14, z],
        "wrist_right": [x, 0.14, z],
    },
]


pose_data_left = [
    {
        "wrist_left": [x, 0.01, z],
        "wrist_right": [x, 0.04, z],
    },
    {
        "wrist_left": [x, 0.10, z],
        "wrist_right": [x, 0.06, z],
    },
]


pose_data_right = [
    {
        "wrist_left": [x, 0.04, z],
        "wrist_right": [x, 0.01, z],
    },
    {
        "wrist_left": [x, 0.06, z],
        "wrist_right": [x, 0.10, z],
    },
]


@pytest.mark.parametrize(
    "pose_data, expected",
    [
        (pose_data_topspin, Spin.TOPSPIN),
        (pose_data_slice, Spin.SLICE),
        (pose_data_flat, Spin.FLAT),
        (pose_data_unknown, Spin.LEARN_TENNIS),
    ],
)
def test_classifiy_spin(pose_data, expected):
    assert classify_spin(pose_data, dominant_hand="left") == expected
    assert classify_spin(pose_data, dominant_hand="right") == expected


@pytest.mark.parametrize(
    "pose_data, expected",
    [
        (pose_data_left, "left"),
        (pose_data_right, "right"),
    ],
)
@pytest.mark.skipif(LEFTY, reason="LEFTY override active")
def test_detect_dominant_hand(pose_data, expected):
    assert detect_dominant_hand(pose_data) == expected


def test_detect_dominant_hand_lefty_override():
    if LEFTY:
        assert detect_dominant_hand(pose_data_right) == "left"
        assert detect_dominant_hand(pose_data_left) == "left"


@pytest.fixture(
    params=[
        (pose_data_left, "left"),
        (pose_data_right, "right"),
    ]
)
def dominant_hand_data(request):
    return request.param


@pytest.mark.skipif(LEFTY, reason="LEFTY override active")
def test_detect_dominant_hand_2(dominant_hand_data):
    pose_data, expected = dominant_hand_data
    assert detect_dominant_hand(pose_data) == expected
