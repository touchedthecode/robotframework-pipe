from typing import Literal
from robot.libraries.BuiltIn import BuiltIn, register_run_keyword
from robot.api.deco import keyword, library
from robot.api import logger
import importlib.metadata


# Decorator to register a method as a Robot Framework keyword variant.
def run_keyword_variant(resolve):
    def decorator(method):
        register_run_keyword(
            "PipeLibrary", method.__name__, resolve, deprecation_warning=False
        )
        return method

    return decorator


@library
class PipeLibrary:
    """Library implementing a pipe operator for keyword chaining.

    This library enhances keyword chaining capabilities in Robot Framework by introducing a pipe operator,
    similar to the one found in functional programming languages. It simplifies the process of passing the
    output of one keyword as an input to another, enabling more readable and maintainable test cases.

    = Table of contents =

    %TOC%

    = Usage =

    The PipeLibrary allows chaining multiple Robot Framework keywords using the `>>` pipe operator.
    It removes the need for intermediate variables, making the data flow between keywords cleaner and more intuitive.

    = Syntax =

    - `Pipe`: The main keyword of the PipeLibrary.
    - `>>`: The pipe operator, used to chain keywords.
    - `Placeholder` (`$` by default): Denotes where the output of the previous keyword should be placed in the next keyword's arguments.

    By default, the result of a keyword is used as the first argument of the next keyword, but this can be customized.

    = Example =

    | `Pipe`    Get User Id    username
    | ...    >>    Fetch User Details
    | ...    >>    Process Data
    | ...    >>    Validate User
    | ...    >>    Log

    = Configuration =

    The library can be initialized with custom settings for `pipe_strategy`, `placeholder`, and `pipe_operator`.

    = Note =

    PipeLibrary does not support keyword syntax highlighting and autocompletion in Robot Framework due to its dynamic nature.

    = Contributions =

    Contributions, bug reports, and suggestions for improvements are welcome. Please visit our GitHub repository.

    """

    ROBOT_LIBRARY_VERSION = importlib.metadata.version("robotframework-pipe")
    ROBOT_LIBRARY_SCOPE = "TEST"
    ROBOT_LIBRARY_FORMAT = "reST"

    def __init__(
        self,
        pipe_strategy: Literal["prepend", "append"] = "prepend",
        placeholder: str = "$",
        pipe_operator: str = ">>",
    ):
        """Initializes the PipeLibrary with optional configuration for piping strategy, placeholder, and operator.

        The `pipe_strategy` can be either 'prepend' or 'append', affecting how the piped result is inserted into the arguments of the next keyword.
        The `placeholder` is a string used in the arguments of keywords to denote where the piped result should be placed.
        The `pipe_operator` is a string used to separate different keywords in a piped sequence.

        Examples:

        | =Setting=   |     =Value=    |   =Value=   |          =Comment=             |
        | Library     | PipeLibrary    |             | # Default prepend strategy     |
        | Library     | PipeLibrary    | append      | # Set strategy to append      |
        """
        self.built_in = BuiltIn()
        self.pipe_strategy = pipe_strategy
        self.placeholder = placeholder
        self.pipe_operator = pipe_operator

    @run_keyword_variant(0)
    @keyword
    def pipe(self, *keywords):
        """Executes a series of Robot Framework keywords in a piped sequence.

        Keywords and their arguments are separated by the `pipe_operator`. The output of each keyword can be passed as input to the next one.

        Example:

        | `Pipe`    Get User Id    username
        | ...    >>    Fetch User Details
        | ...    >>    Process Data
        | ...    >>    Validate User
        | ...    >>    Log

        The piped result from each keyword is passed according to the `pipe_strategy` and can be explicitly referred to using the `placeholder` (`$` by default).

        Example using the placeholder:

        | `Pipe`    Get User Id    username
        | ...    >>    Fetch User Details    $
        | ...    >>    Process Data    $
        | ...    >>    Validate User    $
        | ...    >>    Log    $
        """

        # Split the provided keywords and arguments
        keyword_calls = self._split_pipe_keywords(keywords)

        # Initial value for the piped result
        piped_result = None

        # Execute each keyword in sequence
        for kw, args in keyword_calls:
            if piped_result is not None:
                if self.placeholder in args:
                    # Replace the placeholder with the piped result
                    args = [
                        piped_result if arg == self.placeholder else arg for arg in args
                    ]
                else:
                    if self.pipe_strategy == "append":
                        args.append(piped_result)
                    else:
                        args.insert(0, piped_result)

            try:
                piped_result = self.built_in.run_keyword(kw, *args)
            except Exception as e:
                logger.error(f"Error executing keyword '{kw}': {e}")
                raise

        return piped_result

    def _split_pipe_keywords(self, keywords):
        """Internal method to split the piped keyword sequence into individual keywords and their arguments.

        This method is used by the `pipe` method to process the given sequence of keywords and arguments,
        splitting them based on the `pipe_operator`.

        This is an internal utility method and not exposed as a Robot Framework keyword.
        """
        split_keywords = []
        current_keyword = []
        for item in keywords:
            if item == self.pipe_operator:
                if current_keyword:
                    split_keywords.append((current_keyword[0], current_keyword[1:]))
                    current_keyword = []
            else:
                current_keyword.append(item)
        if current_keyword:
            split_keywords.append((current_keyword[0], current_keyword[1:]))
        return split_keywords
