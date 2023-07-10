import pytest
from CC.hashTables.hashmap_leftJoin import left_join

@pytest.fixture
def synonyms():
    return {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }


@pytest.fixture
def antonyms():
    return {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }


def test_left_join(synonyms, antonyms):
    expected_result = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]
    assert left_join(synonyms, antonyms) == expected_result
