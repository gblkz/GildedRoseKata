from before.gilded_rose import (
    Item,
    update_quality,
)


# Still discovering the best approach: edit the before OR comment but leave as-is.
# Need to stop using comments for note capture.
def test_fixme():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert "fixme" == item.name  # Required change: fixme to foo.
