"""Test suite for the constants module."""

# ruff: noqa: PLR2004

from systemsense import constants


def test_constant_values_for_interface():
    """Ensure that all of the interface constants have a value."""
    assert len(vars(constants.interface).items()) == 8
    for _, value in vars(constants.interface).items():
        assert value is not None


def test_constant_values_for_markers():
    """Ensure that all of the markers constants have a value."""
    assert len(vars(constants.markers).items()) == 2
    for _, value in vars(constants.markers).items():
        assert value is not None


def test_constant_values_for_project():
    """Ensure that all of the project constants have a value."""
    assert len(vars(constants.project).items()) == 4
    for _, value in vars(constants.project).items():
        assert value is not None


def test_constant_values_for_system():
    """Ensure that all of the system constants have a value."""
    assert len(vars(constants.system).items()) == 2
    for _, value in vars(constants.system).items():
        assert value is not None
