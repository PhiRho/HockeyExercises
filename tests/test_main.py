import hockey_exercise.main as Main
import pytest

def test_read_root():
    assert Main.read_root() == {"Hello": "World"}
