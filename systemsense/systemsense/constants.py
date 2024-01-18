"""Define constants with dataclasses."""

from dataclasses import dataclass


# interface constant
@dataclass(frozen=True)
class Interface:
    """Define the Interface dataclass for constant(s)."""

    Welcome_System_Info: str
    Panel_System_Information: str
    Parameter_System: str
    Parameter_Value_System: str
    Welcome_Benchmark_Info: str
    Panel_Benchmark_Information: str
    Parameter_Benchmark: str
    Parameter_Value_Benchmark: str


interface = Interface(
    Welcome_System_Info="✨ Displaying System Information",
    Panel_System_Information="System Information",
    Parameter_System="System Parameter",
    Parameter_Value_System="Parameter Value",
    Welcome_Benchmark_Info="🏁 Displaying Benchmark Results",
    Panel_Benchmark_Information="Benchmark Results",
    Parameter_Benchmark="Benchmark Name",
    Parameter_Value_Benchmark="Benchmark Results (sec)",
)


# markers constants
@dataclass(frozen=True)
class Markers:
    """Define the Markers dataclass for constant(s)."""

    Seconds_Per_Minute: int
    Underscore: str


markers = Markers(
    Underscore="_",
    Seconds_Per_Minute=60,
)


# project constant
@dataclass(frozen=True)
class Project:
    """Define the Project dataclass for constant(s)."""

    Benchmark_Module: str
    Benchmark_Filter: str
    Detect_Module: str
    Detect_Filter: str


project = Project(
    Benchmark_Module="systemsense.benchmark",
    Benchmark_Filter="time_",
    Detect_Module="systemsense.detect",
    Detect_Filter="get_",
)


# system constant
@dataclass(frozen=True)
class System:
    """Define the System dataclass for constant(s)."""

    Arm: str
    Windows: str


system = System(
    Arm="arm",
    Windows="Windows",
)
