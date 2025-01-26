"""Run simple micro-benchmarks for comparing system performance."""

import inspect
import timeit
from typing import Dict, List

from systemsense import constants, execute, util


def benchmark() -> Dict[str, str]:
    """Run all of the sub-benchmarks."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of dictionaries
    # that contain a key-value pair where both are a string;
    # with each entry in the list is an output of one run
    run_output: List[Dict[str, str]] = []
    run_output = execute.execute_by_name_filter(
        constants.project.Benchmark_Module, constants.project.Benchmark_Filter
    )
    # combine all of the dictionaries into a single dictionary
    return util.union_list_of_dicts(run_output)


def benchmark_rangelist(size: int = 100) -> None:
    """Perform a benchmark using the range of a list."""
    _ = [i for i in range(size)]


def time_benchmark_rangelist(
    repeat: int = 3, number: int = 100000, size: int = 100
) -> Dict[str, str]:
    """Time the benchmark_rangelist function."""
    # extract the name of the benchmark function, which
    # is encoded in the name after the second underscore
    function_name = inspect.stack()[0][3].split(constants.markers.Underscore)[
        2
    ]
    # perform the benchmark using the timeit module
    performance_list = timeit.repeat(
        "benchmark.benchmark_rangelist(size)",
        repeat=repeat,
        setup=f"""
from systemsense import benchmark
size = {size}
        """,
        number=number,
    )
    # return a dictionary with the function's
    # name and then the results from the benchmark
    return {function_name: str(performance_list)}


def benchmark_addition(size: int = 100) -> None:
    """Perform a benchmark involving an addition."""
    # initialize the result to zero;
    result = 0
    # add the value of i to the result;
    for i in range(size):
        for _ in range(3):
            result += i
    # for each value of i in the range
    # of the specified size, add it to
    # the running result three times


def time_benchmark_addition(
    repeat: int = 3, number: int = 100000, size: int = 100
) -> Dict[str, str]:
    """Time the benchmark_addition function."""
    # Set up the timer using the timeit module
    setup_code = f"from systemsense.benchmark import benchmark_addition"
    stmt_code = f"benchmark_addition({size})"

    # Run the timer and collect the performance data
    performance_list = timeit.repeat(
        stmt=stmt_code, setup=setup_code, repeat=repeat, number=number
    )

    # Return the results in the required format
    function_name = "benchmark_addition"
    return {function_name: str(performance_list)}


def benchmark_multiplication(size: int = 100) -> None:
    """Perform a benchmark involving a multiplication."""
    # Initialize the result to one (since we're multiplying)
    result = 1
    # For each value of i in the range of the specified size,
    # multiply it together three times and then add it to the running result
    for i in range(size):
        for _ in range(3):
            result *= i


def time_benchmark_multiplication(
    repeat: int = 3, number: int = 100000, size: int = 100
) -> Dict[str, str]:
    """Time the benchmark_multiplication function."""
    setup_code = f"from systemsense.benchmark import benchmark_multiplication"
    stmt_code = f"benchmark_multiplication({size})"

    # Run the timer and collect the performance data
    performance_list = timeit.repeat(
        stmt=stmt_code, setup=setup_code, repeat=repeat, number=number
    )

    # Return the results in the required format
    function_name = "benchmark_multiplication"
    return {function_name: str(performance_list)}


def benchmark_exponentiation(size: int = 100) -> None:
    """Perform a benchmark involving an exponentiation."""
    # initialize the result to zero;
    result = 0
    # add the value of i to the result;
    # for each value of i in the range
    for i in range(size):
        result += i**i
    # of the specified size, compute the value
    # of i to the power of i and then
    # add it to the running result


def time_benchmark_exponentiation(
    repeat: int = 3, number: int = 100000, size: int = 100
) -> Dict[str, str]:
    """Time the benchmark_exponentiation function."""
    setup_code = f"from systemsense.benchmark import benchmark_exponentiation"
    stmt_code = f"benchmark_exponentiation({size})"

    # Run the timer and collect the performance data
    performance_list = timeit.repeat(
        stmt=stmt_code, setup=setup_code, repeat=repeat, number=number
    )

    # Return the results in the required format
    function_name = "benchmark_exponentiation"
    return {function_name: str(performance_list)}


def benchmark_concatenation(size: int = 100) -> None:
    """Perform a benchmark involving an concatenation."""
    result = ""
    for i in range(size):
        for _ in range(3):
            result += str(i)
    # for each value of i in the range
    # of the specified size, add it to
    # the running result three times


def time_benchmark_concatenation(
    repeat: int = 3, number: int = 100000, size: int = 100
) -> Dict[str, str]:
    """Time the benchmark_concatenation function."""
    setup_code = f"from systemsense.benchmark import benchmark_concatenation"
    stmt_code = f"benchmark_concatenation({size})"

    # Run the timer and collect the performance data
    performance_list = timeit.repeat(
        stmt=stmt_code, setup=setup_code, repeat=repeat, number=number
    )

    # Return the results in the required format
    function_name = "benchmark_concatenation"
    return {function_name: str(performance_list)}
