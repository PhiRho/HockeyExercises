import hockey_exercise.main as Main
import pytest

def test_read_root():
    assert Main.read_root() == {"Hello": "World"}

def test_read_item_with_query():
    assert Main.read_item(3, "query string") == {"item_id": 3, "query": "query string"}

def test_read_item_without_query():
    assert Main.read_item(3) == {"item_id": 3, "query": None}

def test_update_item():
    item = Main.Item(name = "name", price = 0.5)
    assert Main.update_item(2, item) == {"item_name": item.name, "item_id": 2}
