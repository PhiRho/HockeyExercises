import hockey_exercise.main
import pytest

def test_read_root():
    assert read_root() == {"Hello": "World"}
