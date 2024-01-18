"""Command-line interface for the systemsense command-line tool."""

import typer
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from systemsense import benchmark, constants, detect

# create a Typer object to support the command-line interface
cli = typer.Typer(no_args_is_help=True)

# create a default console
console = Console()


@cli.command()
def systeminfo() -> None:
    """Detect all relevant information about the system used for experiments."""
    # display a label to indicate what output will appear
    console.print(constants.interface.Welcome_System_Info)
    console.print()
    # detect the system information for all ways
    # in which it is possible to do so as provided
    # by the detect module's functions
    system_info = detect.detect()
    # display the system information in a panel
    # with a rich table inside of it; the keys
    # are in the left-hand column and the values
    # are in the right-hand column
    table = Table(box=box.ROUNDED, show_header=True)
    table.add_column(constants.interface.Parameter_System)
    table.add_column(constants.interface.Parameter_Value_System)
    for label in sorted(system_info.keys()):
        detail = system_info[label]
        table.add_row(label, detail)
    console.print(
        Panel(
            table,
            title=constants.interface.Panel_System_Information,
            expand=True,
        )
    )


@cli.command()
def benchmarkinfo() -> None:
    """Benchmark the system used for experiments."""
    # display a label to indicate what output will appear
    console.print(constants.interface.Welcome_Benchmark_Info)
    console.print()
    # detect the system information for all ways
    # in which it is possible to do so as provided
    # by the detect module's functions
    system_performance = benchmark.benchmark()
    # display the benchmarking information in a panel
    # with a rich table inside of it; the keys
    # are in the left-hand column and the values
    # are in the right-hand column
    table = Table(box=box.ROUNDED, show_header=True)
    table.add_column(constants.interface.Parameter_Benchmark)
    table.add_column(constants.interface.Parameter_Value_Benchmark)
    for label in sorted(system_performance.keys()):
        detail = system_performance[label]
        table.add_row(label, detail)
    console.print(
        Panel(
            table,
            title=constants.interface.Panel_Benchmark_Information,
            expand=True,
        )
    )


@cli.command()
def completeinfo() -> None:
    """Report both the detected system information and the benchmark results."""
    # TODO: Add the code to complete this command, noting that the
    # output from the two sub-commands should be separated by a newline
