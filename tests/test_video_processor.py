import pytest

from tennis_analyzer.video_processor import load_video


def test_load_video_invalid_path():
    with pytest.raises(ValueError):
        load_video("./data/nicht_input.mp4")
