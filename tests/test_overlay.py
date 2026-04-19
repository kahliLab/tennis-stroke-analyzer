import numpy as np
import pytest

from tennis_analyzer.config import ALL_LANDMARKS
from tennis_analyzer.overlay import annotate_frame, draw_lines, put_text


@pytest.fixture
def fake_frame():
    return np.zeros((480, 640, 3), dtype=np.uint8)


@pytest.fixture
def fake_coordinates():
    fake_coordinates = {key: [0.5, 0.3, 0.0] for key in ALL_LANDMARKS.keys()}
    return fake_coordinates


def test_put_text(fake_frame, fake_coordinates):
    spin = "Flat"

    original_frame = fake_frame.copy()
    result_frame = put_text(fake_coordinates, spin, fake_frame)

    assert result_frame is not None
    assert not np.array_equal(original_frame, result_frame)


def test_draw_lines(fake_frame, fake_coordinates):
    spin = "Flat"
    dominant_hand = "left"

    original_frame = fake_frame.copy()
    result_frame = draw_lines(fake_coordinates, fake_frame, spin, dominant_hand)

    assert result_frame is not None
    assert not np.array_equal(original_frame, result_frame)


def test_annotate_frame(fake_frame, fake_coordinates):
    spin = "Flat"
    dominant_hand = "left"

    original_frame = fake_frame.copy()
    result_frame = annotate_frame(spin, fake_frame, fake_coordinates, dominant_hand)

    assert result_frame is not None
    assert not np.array_equal(original_frame, result_frame)
