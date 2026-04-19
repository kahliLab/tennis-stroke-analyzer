import numpy as np
import pytest

from tennis_analyzer.overlay import put_text, draw_lines
from tennis_analyzer.config import ALL_LANDMARKS


@pytest.fixture
def fake_frame():
    return np.zeros((480, 640, 3), dtype=np.uint8)

@pytest.fixture
def fake_coordinates():
    fake_coordinates = {
        key: [0.5, 0.3, 0.0] for key in ALL_LANDMARKS.keys()
    }
    return fake_coordinates
    

def test_put_text(fake_frame, fake_coordinates):
    spin = "Flat"

    original_frame = fake_frame.copy()
    result_frame = put_text(fake_coordinates, spin, fake_frame)

    assert result_frame is not None
    assert not np.array_equal(original_frame, result_frame)
