from app.routers.interactions import _filter_by_item_id
from app.db.interactions import InteractionLog


def test_filter_empty_list_returns_empty():
    """Edge case: filtering an empty list should return empty list."""
    result = _filter_by_item_id([], item_id=1)
    assert result == []


def test_filter_nonexistent_item_id_returns_empty():
    """Filtering by item_id not present should return empty list."""
    interactions = [
        InteractionLog(item_id=2, learner_id=10),
        InteractionLog(item_id=3, learner_id=11),
    ]
    result = _filter_by_item_id(interactions, item_id=999)
    assert result == []


def test_filter_multiple_matching_items():
    """Multiple interactions with same item_id should all be returned."""
    interactions = [
        InteractionLog(item_id=5, learner_id=1),
        InteractionLog(item_id=5, learner_id=2),
        InteractionLog(item_id=6, learner_id=3),
    ]
    result = _filter_by_item_id(interactions, item_id=5)
    assert len(result) == 2
    assert all(i.item_id == 5 for i in result)


def test_filter_does_not_modify_original_list():
    """Function should not mutate original list."""
    interactions = [InteractionLog(item_id=7, learner_id=1)]
    original_length = len(interactions)
    _filter_by_item_id(interactions, item_id=7)
    assert len(interactions) == original_length
