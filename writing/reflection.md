# Algorithmology Setup

## Table of Contents

<!---toc start-->

* [Algorithmology Setup](#algorithmology-setup)
  * [Table of Contents](#table-of-contents)
  * [Gregory M. Kapfhammer](#gregory-m-kapfhammer)
  * [Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."](#re-type-the-sentence-i-adhered-to-the-allegheny-college-honor-code-while-completing-this-project)
  * [Program Output](#program-output)
    * [Report at least five examples of program output to demonstrate that your `systemsense` program works correctly](#report-at-least-five-examples-of-program-output-to-demonstrate-that-your-systemsense-program-works-correctly)
      * [First output from running the `systemsense` program](#first-output-from-running-the-systemsense-program)
      * [Second output from running the `systemsense` program](#second-output-from-running-the-systemsense-program)
      * [Third output from running the `systemsense` program](#third-output-from-running-the-systemsense-program)
      * [Fourth output from running the `systemsense` program](#fourth-output-from-running-the-systemsense-program)
      * [Fifth output from running the `systemsense` program](#fifth-output-from-running-the-systemsense-program)
  * [Experiment Design](#experiment-design)
  * [Experimental Results](#experimental-results)
    * [Results from running `systemsense` on your laptop](#results-from-running-systemsense-on-your-laptop)
    * [Results from running `systemsense` in GitHub Actions](#results-from-running-systemsense-in-github-actions)
  * [Source Code](#source-code)
    * [Describe in detail how the `get_cpufrequencies` function works](#describe-in-detail-how-the-get_cpufrequencies-function-works)
    * [Describe in detail how the `get_battery` function works](#describe-in-detail-how-the-get_battery-function-works)
    * [Describe in detail how the `detect` function works](#describe-in-detail-how-the-detect-function-works)
  * [Professional Development](#professional-development)
    * [Given your experiences during the completion of this project, what do you predict will be challenging when performing algorithm engineering?](#given-your-experiences-during-the-completion-of-this-project-what-do-you-predict-will-be-challenging-when-performing-algorithm-engineering)
    * [Why is it necessary to detect the parameters of a system before running experiments?](#why-is-it-necessary-to-detect-the-parameters-of-a-system-before-running-experiments)
    * [What could happen if you did not thoroughly test a function before evaluating its performance?](#what-could-happen-if-you-did-not-thoroughly-test-a-function-before-evaluating-its-performance)
    * [How do the empirical results suggest that you don't yet know the entire story about the performance results from the micro-benchmarks?](#how-do-the-empirical-results-suggest-that-you-dont-yet-know-the-entire-story-about-the-performance-results-from-the-micro-benchmarks)
  * [Take Home Points](#take-home-points)

<!---toc end-->

TODO: Make sure that you remove all the markers in this file that serve a
prompts for work that you have not yet completed. The final version of this
report should be written as if it was a scientific report that you could publish
on the Algorithmology web site or in a scientific journal.

## Gregory M. Kapfhammer

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

TODO: You must retype the sentence here in order to digitally sign your pledge.

"I adhered to the Allegheny College Honor Code while completing this project."

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

TODO: Please list here the sources that you consulted while completing the
algorithm engineering project! The list of sources should also include
references to any artificial intelligence coding assistants that you used and a
summary of the ways in which you used those coding assistants to complete this
project.

## Program Output

### Report at least five examples of program output to demonstrate that your `systemsense` program works correctly

TODO: Please provide five examples of program output from running the command
`poetry run systemsense completeinfo` so as to clearly report that (i) the data
collected in the first table (i.e., the table that provides the `System
Information`) does not vary across program runs and (ii) the data collected in
the second table (i.e., the table that provides the `Benchmark Results`) does
vary across program runs.

TODO: Please make sure that some of the provided data comes from running
`systemsense` on your laptop and some of the provided data comes from running it
in GitHub Actions. You should write a sentence before each output sample to make
it clear where the data comes from. You may not hand-edit and of the program
outputs that you provide in this report.

TODO: Please provide the output from running the program in fenced code blocks
within each of the following subsections.

#### First output from running the `systemsense` program

#### Second output from running the `systemsense` program

#### Third output from running the `systemsense` program

#### Fourth output from running the `systemsense` program

#### Fifth output from running the `systemsense` program

## Experiment Design

TODO: Pick at least one detection function provided by `systemsense` in `detect.py`
and answer these questions:

- What is the name of the function?
- What parameter does this function detect?
- How does this function detect this parameter?
- What are the pitfalls associated with detecting this parameter?
- What are the implications of detecting this parameter?
- What are the best ways to communicate this detected parameter?

TODO: Please provide your responses to this in a list.

TODO: Pick at least one micro-benchmark provided by `systemsense` in `benchmark.py`
and answer these questions:

- What is the name of the function?
- What value does this function measure?
- How does this function measure this value?
- What are the pitfalls associated with measuring this value?
- What are the implications of measuring this value?
- What are the best ways to communicate this measured value?

TODO: Please provide your responses to this in a list.

TODO: For both of these prompts, please do not answer the questions for source
code that is already provided inside of this file!

## Experimental Results

### Results from running `systemsense` on your laptop

TODO: Please write at least one paragraph to identify an experimental trend and
to explain why this trend is evident in the results.

### Results from running `systemsense` in GitHub Actions

TODO: Please write at least one paragraph to identify an experimental trend and
to explain why this trend is evident in the results.

## Source Code

TODO: For each of the provide source code segments, please provide a thorough
description of the program's behavior. Your description of the function should
go beyond the provided comments by explaining precisely how the called functions
work and commenting on the suitability of the function's design for its purpose.

### Describe in detail how the `get_cpufrequencies` function works

TODO: Write at least one paragraph to explain the request source code

```python
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

```

### Describe in detail how the `get_battery` function works

TODO: Write at least one paragraph to explain the provided source code

```python
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
```

### Describe in detail how the `detect` function works

TODO: Write at least one paragraph to explain the provided source code

```python
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
```

## Professional Development

### Given your experiences during the completion of this project, what do you predict will be challenging when performing algorithm engineering?

TODO: Write at least one paragraph that answers this question in your own words.

### Why is it necessary to detect the parameters of a system before running experiments?

TODO: Write at least one paragraph that answers this question in your own words.

### What could happen if you did not thoroughly test a function before evaluating its performance?

TODO: Write at least one paragraph that answers this question in your own words.

### How do the empirical results suggest that you don't yet know the entire story about the performance results from the micro-benchmarks?

TODO: Write at least one paragraph that answers this question in your own words.

## Take Home Points

TODO: Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course web site and use them to facilitate
follow-on class discussions.
