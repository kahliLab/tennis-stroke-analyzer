import pytest
from dataclasses import dataclass

from tennis_analyzer.pose_tracker import get_coordinates


@dataclass
class FakeLandmark:
    x: float
    y: float
    z: float


class FakeLandmarks:
    def __init__(self):
        self.landmark = [FakeLandmark(0.5, 0.5, 0.5)] * 33


@pytest.fixture
def fake_landmarks():
    return FakeLandmarks()

def test_get_coordinates(fake_landmarks):
    result = get_coordinates(fake_landmarks)

    helper_body_parts_index = {
        "shoulder_left": 11,
        "shoulder_right": 12,
        "elbow_left": 13,
        "elbow_right": 14,
        "wrist_left": 15,
        "wrist_right": 16,
    }
    assert len(result) == len(helper_body_parts_index)

    for key, value in result.items():
        assert key in helper_body_parts_index.keys()
        assert value == [0.5, 0.5, 0.5]
