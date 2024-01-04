# robotframework-pipe

[![Version](https://img.shields.io/pypi/v/robotframework-pipe.svg)](https://pypi.org/project/robotframework-pipe/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

Pipe is a Robot Framework Library that brings the pipe operator known from functional programming languages into Robot Framework. PipeLibrary is designed to enhance keyword chaining capabilities, it simplifies the process of passing the output of one keyword as an input to another, enabling more readable and maintainable test cases.

## Installation

To install PipeLibrary, run the following command:

```bash
pip install robotframework-pipe
```

## Usage

Here's a basic example to demonstrate the usage of the PipeLibrary:

```RobotFramework
*** Settings ***
Library    PipeLibrary

*** Test Cases ***
Complex Operation With Pipe
    Pipe    Get User Id    username
    ...    >>    Fetch User Details
    ...    >>    Process Data
    ...    >>    Validate User
    ...    >>    Log
```

Without Pipe, the same example would require intermediate variables:

```RobotFramework
Complex Operation Without Pipe
    ${user_id} =    Get User Id    username
    ${user_details} =    Fetch User Details    ${user_id}
    ${processed_data} =    Process Data    ${user_details}
    ${status} =    Validate User    ${processed_data}
    Log    ${status}
```

The PipeLibrary simplifies the process by removing the need for intermediate variables and making the flow of data between keywords more intuitive and cleaner.

### Syntax Explanation

- `Pipe`: The main keyword of the PipeLibrary.
- `>>`: The pipe operator, used to chain keywords.
- `Placeholder`: A symbol (default `$`) used to denote where the output of the previous keyword should be placed in the next keyword's argument list. This is optional.

By default, the result of the keyword is used as the _first_ argument of the next keyword. You can use the Placeholder to explicitly set the argument or import the PipeLibrary with the argument `pipe_strategy=append` to use the result as the _last_ argument by default.

## Examples

You can find more examples in the `/tests` directory.

### Using Placeholder

```RobotFramework
My Test Case
    Pipe    Sum    1    2
    ...    >>    Subtract    4    $
    ...    >>    Should be Equal As Integers    1
```

In this example, `$` is replaced with the result of Sum, so Subtract is called as `Subtract    4    3`.

## Configuration

You can initialize the library with custom settings:

```RobotFramework
*** Settings ***
Library    PipeLibrary    pipe_strategy=append    placeholder=$    pipe_operator=>>
```

## Note

Currently, PipeLibrary does not support keyword syntax highlighting and autocompletion in the Robot Framework environment. This is due to the dynamic nature of the pipe operator and the way arguments are passed between keywords.

## Contributions

Contributions to PipeLibrary are welcome! If you have suggestions for improvements or have identified a bug, please feel free to open an issue or submit a pull request on our GitHub repository.
