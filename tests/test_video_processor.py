import numpy as np
import pytest

from tennis_analyzer.video_processor import load_video, extract_frames


def test_load_video_invalid_path():
    with pytest.raises(ValueError):
        load_video("./data/nicht_input.mp4")


class FakeCap:
    def __init__(self, frames):
        self.frames = frames
        self.index = 0

    def read(self):
        if self.index < len(self.frames):
            frame = self.frames[self.index]
            self.index += 1
            return (True, frame)
        else:
            return (False, None)

    def release(self):
        pass


@pytest.fixture
def fake_frame():
    return np.zeros((480, 640, 3), dtype=np.uint8)


@pytest.fixture
def fake_cap(fake_frame):
    return FakeCap([fake_frame])


def test_extract_frames(fake_cap):
    frames = extract_frames(fake_cap)
    assert isinstance(frames, list)