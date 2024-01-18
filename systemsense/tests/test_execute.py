"""Test suite for the execute module."""

from systemsense import execute


def test_execute_by_name_filter_systemsense_detect():
    """Ensure that the return type is correct for all functions."""
    result = execute.execute_by_name_filter("systemsense.detect", "get_")
    assert result is not None
    assert isinstance(result, list)
    assert isinstance(next(iter(result[0].keys())), str)
    assert isinstance(next(iter(result[0].values())), str)
