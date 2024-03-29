from after.gilded_rose import (
    Item,
    update_quality,
)

AGED_BRIE = "Aged Brie"


# Watch Arjan's video PyTest unit testing, then extend these and integrate with automation.
# Watch for how Arjan executes his tests, then replicate for this project.
def test_item_doesnt_change_name():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert "foo" == item.name  # Only test from before.


def test_item_sell_in_decreases():
    item = Item("foo", 1, 0)
    update_quality([item])
    assert 0 == item.sell_in


def test_item_quality_decreases():
    item = Item("foo", 0, 1)
    update_quality([item])
    assert 0 == item.quality


def test_item_quality_is_never_negative():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert 0 == item.quality


def test_item_quality_is_never_more_than_50():
    item = Item(AGED_BRIE, 0, 50)
    update_quality([item])
    assert 50 == item.quality


def test_item_quality_degrades_twice_as_fast_after_sell_in():
    item = Item("foo", 0, 10)
    update_quality([item])
    assert 8 == item.quality
