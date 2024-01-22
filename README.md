# 🔬 Algorithmology System Sense

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Algorithmology System Sense](#-algorithmology-system-sense)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)
  * [🎉 Program Specifications](#-program-specifications)
  * [🐶 Project Reflection](#-project-reflection)
  * [🐊 Project Assessment](#-project-assessment)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date. Please note
that the content provided in the `README.md` file for this GitHub repository is
an overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project. Finally, it is important to point out that your
repository for this project was created from the GitHub repository template
called
[algorithmology-setup-starter](https://github.com/Algorithmology/algorithmology-setup-starter),
you can check this repository for any updates to this project's documentation or
source code!

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

The purpose of this assignment is to produce and report on the results from
running a program called `systemsense`.  This final version of this program must
support (i) collecting information about the system that ran the program and
(ii) running some micro-benchmarks to collect data about the performance of the
computer that runs the program. After cloning this repository to your computer,
please take the following steps to get started on the project:

- To install the necessary software for running the `systemsense` program that
you will create as a part of this project, you should install the
[`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind that it is
not necessary for you to install the `cachix` program referenced by these
installation instructions. Please note that students who are using Windows 11
should first install Windows subsystem for Linux (`wsl2`) before attempting to
install `devenv`. Once you have installed `devenv` and cloned this repository to
your computer, you can `cd` into the directory that contains the
`pyproject.toml` file and then type `devenv shell`. It is important to note that
the first time you run this command it may complete numerous steps and take a
considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains Python `3.11.6` and Poetry `1.7.1`! You can verify
that you have the correct version of these two programs by typing:
  - `python --version` (note that you should see `3.11.6`)
  - `poetry --version` (note that you should see `1.7.1`)
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop. With
that said, please make sure that you only use the specified versions of Python
and Poetry to complete this project. This means that, to ensure that the results
from running the micro-benchmarks are consistent and, as best as is possible,
comparable to the results from other computers, you should use exactly the
specified version of either Python or Poetry.
- Before moving to the next step, you may need to again type `poetry install` in
order to avoid the appearance of warnings when you next run the `systemsense`
program. Now you can type the command `poetry run systemsense --help` and
explore how to use the program.

## 🎉 Program Specifications

- Please note that the program will not work unless you add the required source
code at the designated `TODO` markers.
- Once you have added all of the required functionality, it should produce
output like the following when you run the command `poetry run systemsense
completeinfo`:

```text
✨ Displaying System Information

╭────────────────────────────────────────────────── System Information ──────────────────────────────────────────────────╮
│ ╭──────────────────┬────────────────────────────────────────────────────────────────────────╮                          │
│ │ System Parameter │ Parameter Value                                                        │                          │
│ ├──────────────────┼────────────────────────────────────────────────────────────────────────┤                          │
│ │ battery          │ 100% battery life remaining, unknown seconds remaining                 │                          │
│ │ cpu              │ x86_64                                                                 │                          │
│ │ cpucores         │ 12 cores                                                               │                          │
│ │ cpufrequencies   │ Min: 400.0 Mhz, Max: 5325.0 Mhz                                        │                          │
│ │ datetime         │ 2024-01-18 08:47:32.332148                                             │                          │
│ │ disk             │ Using 49.47 GB of 1822.85 GB                                           │                          │
│ │ hostname         │ diameno                                                                │                          │
│ │ memory           │ Using 7.39 GB of 58.56 GB                                              │                          │
│ │ platform         │ Linux-6.6.7-x86_64-with-glibc2.38                                      │                          │
│ │ pythonversion    │ 3.11.6                                                                 │                          │
│ │ runningprocesses │ 410 running processes                                                  │                          │
│ │ swap             │ Using 0.00 GB of 0.00 GB                                               │                          │
│ │ system           │ Linux                                                                  │                          │
│ │ systemload       │ Average Load: 0.44, CPU Utilization: 9.10%                             │                          │
│ │ virtualenv       │ /home/gkapfham/.cache/pypoetry/virtualenvs/systemsense-aoTH3cGV-py3.11 │                          │
│ ╰──────────────────┴────────────────────────────────────────────────────────────────────────╯                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🏁 Displaying Benchmark Results

╭────────────────────────────────────────────────── Benchmark Results ───────────────────────────────────────────────────╮
│ ╭────────────────┬─────────────────────────────────────────────────────────────────╮                                   │
│ │ Benchmark Name │ Benchmark Results (sec)                                         │                                   │
│ ├────────────────┼─────────────────────────────────────────────────────────────────┤                                   │
│ │ addition       │ [0.277979521000816, 0.26007915000081994, 0.260105178997037]     │                                   │
│ │ concatenation  │ [0.5054890969986445, 0.5036637520024669, 0.5107707299976028]    │                                   │
│ │ exponentiation │ [1.7947803429997293, 1.7929458879953017, 1.7814490309974644]    │                                   │
│ │ multiplication │ [0.36264725199725945, 0.3605323439987842, 0.3609781139966799]   │                                   │
│ │ rangelist      │ [0.11802417500439333, 0.11804051499348134, 0.11748810599965509] │                                   │
│ ╰────────────────┴─────────────────────────────────────────────────────────────────╯                                   │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

- You should confirm that the program is producing the expected output by
comparing it to the previous output segment. With that said, it is important to
note that each student's laptop will likely produce different performance
results when running this program! You should also check the output that the
program produces when it is run on Windows, MacOS, and Linux through GitHub
Actions.
- It is also possible that certain features of this program may lead to crashes
or system instability when it is run on certain laptops or operating systems. At
minimum, you need to confirm that the program works correctly in all execution
environments that are used through GitHub Actions. You should also ensure that
the program runs without crashing on your laptop. If you find a circumstance in
which the program cannot correctly collect information about your system, please
add exception handling code to catch any exceptions or errors and then report
back default information about the system.
- Along with implementing the `systemsense` program so that it produces the
expected output you must ensure that it passes a wide variety of static analyses
that confirm that the source code has, for instance, suitable docstrings and
type annotations for every function.
- You also need to ensure that each function, excepting those functions in
`main.py`, has one or more test cases that execute all of the statements and
branches in an attempt to ensure that there are no lingering defects.
Importantly, this means that you will need to add test cases to the provided
test suite so as to guarantee that you achieve the required test coverage goal
for the test suite.
- If any of the static analysis or test cases do not pass or your test suite
does not achieve the required test coverage goal then your GitHub Actions builds
will not pass.

## 🐶 Project Reflection

As you are implementing, testing, and running the `systemsense` program, you
should also complete all of the writing assignments in the
`writing/reflection.md` file. Please make sure that you also completely delete
every `TODO` marker and its label from every line of the `writing/reflection.md`
file. This means that you should not simply delete the `TODO` marker but instead
delete the entire prompt so that your reflection is a document that contains
polished technical writing that is suitable for publication on your professional
web site. Here are some other points to consider as you work on the reflection:

- Unless specified otherwise, you should not include program output in the
reflection that did not arise from you running the program on your laptop.
Critically, you should never hand-edit any of the program output that you insert
into the reflection. This means that all of the output that you include in your
reflection should be copied directly from your computer's terminal window.
- All of the technical writing in your reflection should have correct Markdown
syntax and correctly display inside of GitHub.
- The writing in your reflection should be free from spelling and grammar
mistakes.
- The reflection should always conclude with between two and three sentences
that explain the key take-home points that you have learned during the
completion of this project.

## 🐊 Project Assessment

Please keep in mind the following reminders as you consider how the course
instructor will assess the final version of your project:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
Please note that if all of the GatorGrader checks do not pass, then your GitHub
Actions build will not pass either. You need to make sure that you have a
passing build in GitHub Actions before the project's due date.
- The GitHub repository that houses this project has a GitHub Actions
configuration that will report to you through the GitHub Actions tab a summary
of the key results from running the assessment. You can check this tab to
quickly see which the status of the GatorGrader checks and to review a report
about the coverage of the test suite that accompanies the project.
- Don't forget to provide all of the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code and technical writing. This means
that instead of only deleting the `TODO` marker from the file you should delete
the `TODO` marker and the entire prompt and then add your own content to
demonstrate that you understand all aspects of this project.
