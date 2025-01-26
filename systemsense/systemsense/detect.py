"""Detect information about the system to support contextualization of experimental results."""

import inspect
import sys
import os
import platform
import socket
from datetime import datetime
from typing import Dict, List

import psutil

from systemsense import constants, execute, util


def detect() -> Dict[str, str]:
    """Run all of the sub-detects."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of dictionaries
    # that contain a key-value pair where both are a string;
    # with each entry in the list is an output of one run
    run_output: List[Dict[str, str]] = []
    run_output = execute.execute_by_name_filter(
        constants.project.Detect_Module, constants.project.Detect_Filter
    )
    # combine all of the dictionaries into a single dictionary
    return util.union_list_of_dicts(run_output)


def get_battery() -> Dict[str, str]:
    """Return information about the current power/battery in the system."""
    # detect the name of the function in
    # which this source code exists
    function_name = inspect.stack()[0][3]
    # parse out the second part of the name after
    # the underscore character
    function_name = function_name.split("_")[1]
    # detect the power/battery information
    battery = psutil.sensors_battery()
    # if the battery is not present, then
    # return a message indicating that
    if battery is None:
        return {function_name: "No battery is present"}
    else:
        # convert the number of seconds to
        # a human-readable format; note that this
        # value may be negative if the battery
        # is charging and/or not discharging
        if battery.secsleft < 0:
            battery_life = "unknown seconds remaining"
        # there is a specific estimate of the number of seconds
        # remaining for the battery's current charge
        else:
            battery_life = (
                util.convert_seconds_to_hours(battery.secsleft)
                + " seconds remaining"
            )
        # extract the percentage of battery remaining
        battery_percent = battery.percent
        # create a final formatted string that includes:
        # 1) the percentage of battery remaining
        # 2) the number of seconds remaining
        battery = (
            f"{battery_percent:.2f}% battery life remaining, {battery_life}"
        )
        # create a dictionary with the function's
        # purpose as the key and the value as
        # the return of the function that collects it
        return {function_name: str(battery)}


def get_cpu() -> Dict[str, str]:
    """Return information about the current CPU in the system."""
    # Detect the name of the function in which this source code exists
    function_name = inspect.stack()[0][3]
    # Parse out the second part of the name after the underscore character
    function_name = function_name.split("_")[1]

    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Create a formatted string with CPU usage
    function_value = f"CPU Usage: {cpu_percent:.2f}%"

    # Return the function's purpose as the key and the CPU information as the value
    return {function_name: function_value}


def get_cpucores() -> Dict[str, str]:
    """Return information about CPU cores within the system."""
    # Detect the name of the function in which this source code exists
    function_name = inspect.stack()[0][3]
    # Parse out the second part of the name after the underscore character
    function_name = function_name.split("_")[1]

    # Get the count of logical CPUs and physical cores
    logical_cpus = psutil.cpu_count(logical=True)
    physical_cores = psutil.cpu_count(logical=False)

    # Create a formatted string with CPU core details
    function_value = (
        f"Logical CPUs: {logical_cpus}, Physical Cores: {physical_cores}"
    )

    # Return the function's purpose as the key and the core details as the value
    return {function_name: function_value}


def get_cpufrequencies() -> Dict[str, str]:
    """Return information about CPU frequency for the system."""
    # detect the name of the function in
    # which this source code exists
    function_name = inspect.stack()[0][3]
    # parse out the second part of the name after
    # the underscore character
    function_name = function_name.split("_")[1]
    # create a dictionary with the function's
    # purpose as the key and the value as
    # the return of the function that collects it
    # performing the detection running on an Apple
    # Silicon leads to crashes even with the most
    # recent versions of psutil, thus return no
    # information only on this platform
    # Reference: https://github.com/giampaolo/psutil/issues/1892
    if platform.processor() == constants.system.Arm:
        cpu_freqs_display = "Min: Unknown Mhz, Max: Unknown Mhz"
    # otherwise, perform the detection on all other platforms
    else:
        # try to detect the CPU frequencies and
        # if there is an error, then return a message
        try:
            cpu_freqs = psutil.cpu_freq()
            cpu_freqs_display = (
                f"Min: {cpu_freqs.min} Mhz, Max: {cpu_freqs.max} Mhz"
            )
        # detection of CPU frequencies failed, which is
        # possible for a wide variety of reasons
        except Exception as _:
            cpu_freqs_display = "Min: Unknown Mhz, Max: Unknown Mhz"
    # return the final dictionary with the
    # function's name and the min/max CPU frequencies
    return {function_name: str(cpu_freqs_display)}


def get_datetime() -> Dict[str, str]:
    """Return the current datetime on the system."""
    # Detect the name of the function in which this source code exists
    function_name = "datetime"

    # Get the current date and time in a human-readable format
    function_value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the function's purpose as the key and the datetime as the value
    return {function_name: function_value}


def get_disk() -> Dict[str, str]:
    """Return disk space usage."""
    # Detect the name of the function in which this source code exists
    function_name = "disk"

    # Retrieve disk usage statistics for the root directory
    try:
        disk_usage = psutil.disk_usage("/")
        function_value = (
            f"Total: {disk_usage.total // (1024**3)} GB, "
            f"Used: {disk_usage.used // (1024**3)} GB, "
            f"Free: {disk_usage.free // (1024**3)} GB, "
            f"Percentage: {disk_usage.percent}%"
        )
    except Exception as e:
        function_value = f"Error retrieving disk usage: {e}"

    # Return a dictionary with the function name and the disk usage details
    return {function_name: function_value}


def get_hostname() -> Dict[str, str]:
    """Return the hostname of the system."""
    function_name = "hostname"
    try:
        function_value = socket.gethostname()
    except Exception as e:
        function_value = f"Error retrieving hostname: {e}"
    return {function_name: function_value}


def get_memory() -> Dict[str, str]:
    """Return the memory usage of the system."""
    function_name = "memory"
    try:
        memory = psutil.virtual_memory()
        function_value = (
            f"Total: {memory.total // (1024**3)} GB, "
            f"Available: {memory.available // (1024**3)} GB, "
            f"Used: {memory.used // (1024**3)} GB, "
            f"Percentage: {memory.percent}%"
        )
    except Exception as e:
        function_value = f"Error retrieving memory: {e}"
    return {function_name: function_value}


def get_platform() -> Dict[str, str]:
    """Return the current platform of the system."""
    function_name = "platform"
    try:
        function_value = platform.platform()
    except Exception as e:
        function_value = f"Error retrieving platform: {e}"
    return {function_name: function_value}


def get_pythonversion() -> Dict[str, str]:
    """Return the current Python version on the system."""
    function_name = "pythonversion"
    try:
        function_value = sys.version
    except Exception as e:
        function_value = f"Error retrieving Python version: {e}"
    return {function_name: function_value}


def get_runningprocesses() -> Dict[str, str]:
    """Return the total number of processes running on the system."""
    function_name = "runningprocesses"
    try:
        function_value = str(len(psutil.pids()))
    except Exception as e:
        function_value = f"Error retrieving running processes: {e}"
    return {function_name: function_value}


def get_system() -> Dict[str, str]:
    """Return the system type and release."""
    function_name = "system"
    try:
        function_value = f"{platform.system()} {platform.release()}"
    except Exception as e:
        function_value = f"Error retrieving system information: {e}"
    return {function_name: function_value}


def get_systemload() -> Dict[str, str]:
    """Return the system load averages."""
    function_name = "systemload"
    try:
        load = (
            psutil.getloadavg() if hasattr(psutil, "getloadavg") else (0, 0, 0)
        )
        function_value = (
            f"1 min: {load[0]}, 5 min: {load[1]}, 15 min: {load[2]}"
        )
    except Exception as e:
        function_value = f"Error retrieving system load: {e}"
    return {function_name: function_value}


def get_swap() -> Dict[str, str]:
    """Return information about swap space usage."""
    function_name = "swap"
    try:
        swap = psutil.swap_memory()
        function_value = (
            f"Total: {swap.total // (1024**3)} GB, "
            f"Used: {swap.used // (1024**3)} GB, "
            f"Free: {swap.free // (1024**3)} GB, "
            f"Percentage: {swap.percent}%"
        )
    except Exception as e:
        function_value = f"Error retrieving swap space: {e}"
    return {function_name: function_value}


def get_virtualenv() -> Dict[str, str]:
    """Return the virtual environment hosting this process."""
    function_name = "virtualenv"
    try:
        function_value = os.getenv(
            "VIRTUAL_ENV", "No virtual environment detected"
        )
    except Exception as e:
        function_value = f"Error detecting virtual environment: {e}"
    return {function_name: function_value}
