import numpy as np
import pytest

from tennis_analyzer.overlay import put_text


@pytest.fixture
def fake_frame():
    return np.zeros((480, 640, 3), dtype=np.uint8)


def test_put_text(fake_frame):
    fake_coordinates = {"nose": [0.5, 0.3, 0.0]}
    spin = "Flat"
    
    original_frame = fake_frame.copy()
    result_frame = put_text(fake_coordinates, spin, fake_frame)

    assert result_frame is not None
    assert not np.array_equal(original_frame, result_frame)
