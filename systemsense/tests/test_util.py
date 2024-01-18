"""Test suite for the util module."""

# ruff: noqa: PLR2004

import pytest

from systemsense import util


@pytest.fixture
def input_list_of_dicts():
    """Create a test fixture for a list of dictionaries with no duplicates."""
    return [{"a": "1"}, {"b": "2"}, {"c": "3"}, {"d": "4"}]


@pytest.fixture
def input_list_of_dicts_duplicates():
    """Create a test fixture for a list of dictionaries with duplicates."""
    return [
        {"a": "1"},
        {"b": "2"},
        {"c": "3"},
        {"d": "4"},
        {"d": "5"},
        {"a": "1"},
    ]


def test_return_type(input_list_of_dicts):
    """Confirm that the return type is correct."""
    result = util.union_list_of_dicts(input_list_of_dicts)
    assert isinstance(result, dict)


def test_union_keys(input_list_of_dicts):
    """Confirm that the keys are correct in the union."""
    result = util.union_list_of_dicts(input_list_of_dicts)
    assert set(result.keys()) == {"a", "b", "c", "d"}


def test_union_values(input_list_of_dicts):
    """Confirm that the correct values are inside of the unioned dict."""
    result = util.union_list_of_dicts(input_list_of_dicts)
    assert len(set(result.values())) == 4
    # confirm that the key values pairs are in the union
    assert result["a"] == "1"
    assert result["b"] == "2"
    assert result["c"] == "3"
    assert result["d"] == "4"


def test_union_values_with_duplicates(input_list_of_dicts_duplicates):
    """Confirm that the correct values are inside of the unioned dict."""
    result = util.union_list_of_dicts(input_list_of_dicts_duplicates)
    # note that union will strip away duplicate key-value pairs
    assert len(set(result.values())) == 4
    # confirm that the key values pairs are in the union
    # note that union will only keep the second occurence
    # of the key-value pair of the same key
    assert result["a"] == "1"
    assert result["b"] == "2"
    assert result["c"] == "3"
    assert result["d"] == "5"


def test_empty_input():
    """Confirm that the union of an empty list of no dicts is an empty dict."""
    result = util.union_list_of_dicts([])
    assert result == {}


def test_seconds_to_human_readable():
    """Confirm that it is possible to confirm seconds to a humanreadable format."""
    # reference: https://psutil.readthedocs.io/en/latest/#system-related-functions
    seconds_remaining = 16628
    result = util.convert_seconds_to_hours(seconds_remaining)
    assert result == "4:37:08"
