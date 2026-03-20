import pytest
from dataclasses import dataclass

from src.tennis_analyzer.pose_tracker import get_coordinates


@dataclass
class FakeLandmark:
    x: float
    y: float
    z: float


class FakeLandmarks:
    def __init__(self):
        self.landmakr = [FakeLandmark(0.5, 0.5, 0.5)] * 33
