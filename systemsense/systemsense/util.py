"""Utility functions for the systemsetup project."""

from typing import Dict, List

from systemsense import constants


def convert_seconds_to_hours(seconds: int) -> str:
    """Convert seconds to hours, minutes, and seconds."""
    # reference: https://psutil.readthedocs.io/en/latest/#system-related-functions
    mm, ss = divmod(seconds, constants.markers.Seconds_Per_Minute)
    hh, mm = divmod(mm, constants.markers.Seconds_Per_Minute)
    return "%d:%02d:%02d" % (hh, mm, ss)


def union_list_of_dicts(container: List[Dict[str, str]]) -> Dict[str, str]:
    """Union a list of dictionaries into a single dictionary."""
    # define the output dictionary
    output: Dict[str, str] = {}

    # iterate over each dictionary in the list
    for d in container:
        # update the output dictionary with the current dictionary
        output.update(d)

    return output  # return ouput
