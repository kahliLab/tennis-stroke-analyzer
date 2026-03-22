import pytest
from dataclasses import dataclass

from tennis_analyzer.pose_tracker import get_coordinates, get_body_parts


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

    body_parts = get_body_parts()

    assert len(result) == len(body_parts)

    for key, value in result.items():
        assert key in body_parts.keys()
        assert value == [0.5, 0.5, 0.5]
