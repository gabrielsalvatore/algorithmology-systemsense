"""Test suite for the benchmark module."""

from systemsense import benchmark


def test_time_benchmark_output_rangelist():
    """Confirm that the rangelist benchmark returns valid data."""
    result = benchmark.time_benchmark_rangelist(repeat=1, number=10, size=10)
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)
    assert isinstance(next(iter(result.values())), str)


def test_time_benchmark_output_addition():
    """Confirm that the addition benchmark returns valid data."""
    result = benchmark.time_benchmark_addition(repeat=1, number=10, size=10)
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)
    assert isinstance(next(iter(result.values())), str)


def test_time_benchmark_output_multiplication():
    """Confirm that the multiplication benchmark returns valid data."""
    result = benchmark.time_benchmark_multiplication(
        repeat=1, number=10, size=10
    )
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)
    assert isinstance(next(iter(result.values())), str)


def test_time_benchmark_output_exponentiation():
    """Confirm that the exponentiation benchmark returns valid data."""
    result = benchmark.time_benchmark_exponentiation(
        repeat=1, number=10, size=10
    )
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)
    assert isinstance(next(iter(result.values())), str)


def test_time_benchmark_output_concatenation():
    """Confirm that the concatenation benchmark returns valid data."""
    result = benchmark.time_benchmark_concatenation(
        repeat=1, number=10, size=10
    )
    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(next(iter(result.keys())), str)
    assert isinstance(next(iter(result.values())), str)
