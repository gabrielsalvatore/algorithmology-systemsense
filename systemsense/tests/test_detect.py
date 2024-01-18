"""Test cases for the detect module."""

import pytest

from systemsense import detect


# parameterize test over all detect functions, including the one
# that recursively runs all of the other functions in the detect module
@pytest.mark.parametrize(
    "function_name",
    [
        "detect",
        "get_battery",
        "get_cpu",
        "get_cpucores",
        "get_cpufrequencies",
        "get_datetime",
        "get_hostname",
        "get_memory",
        "get_platform",
        "get_pythonversion",
        "get_system",
        "get_swap",
        "get_virtualenv",
    ],
)
def test_all_function_outputs(function_name):
    """Ensure that the return type is correct for all functions."""
    func = getattr(detect, function_name)
    result = func()
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)


def test_get_key_battery():
    """Ensure that the return value has the correct key name."""
    result = detect.get_battery()
    assert "battery" in result


def test_get_key_cpu():
    """Ensure that the return value has the correct key name."""
    result = detect.get_cpu()
    assert "cpu" in result


def test_get_key_cpucores():
    """Ensure that the return value has the correct key name."""
    result = detect.get_cpucores()
    assert "cpucores" in result


def test_get_key_cpufrequencies():
    """Ensure that the return value has the correct key name."""
    result = detect.get_cpufrequencies()
    assert "cpufrequencies" in result


def test_get_key_datetime():
    """Ensure that the return value has the correct key name."""
    result = detect.get_datetime()
    assert "datetime" in result


def test_get_key_hostname():
    """Ensure that the return value has the correct key name."""
    result = detect.get_hostname()
    assert "hostname" in result


def test_get_key_memory():
    """Ensure that the return value has the correct key name."""
    result = detect.get_memory()
    assert "memory" in result


def test_get_key_platform():
    """Ensure that the return value has the correct key name."""
    result = detect.get_platform()
    assert "platform" in result


def test_get_key_pythonversion():
    """Ensure that the return value has the correct key name."""
    result = detect.get_pythonversion()
    assert "pythonversion" in result


def test_get_key_swap():
    """Ensure that the return value has the correct key name."""
    result = detect.get_swap()
    assert "swap" in result


def test_get_key_system():
    """Ensure that the return value has the correct key name."""
    result = detect.get_system()
    assert "system" in result
