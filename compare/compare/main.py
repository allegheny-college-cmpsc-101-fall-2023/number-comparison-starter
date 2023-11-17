"""Perform number comparison to find the largest odd number."""

# TODO: make sure that you resolve all of the TODO markers inside
# of this file. Once you are done with a TODO marker you should
# either delete it and rewrite the comment or delete the entire comment

from typing import Tuple
from typing import List
from pathlib import Path

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()


def get_minimum(first: int, second: int, third: int) -> int:
    """Determine the smallest of the three provided values."""
    # TODO: write a function body that will return the smallest of
    # the three formal parameters to this function
    # There are multiple correct solutions.


def get_largest_odd(first: int, second: int, third: int) -> Tuple[int, bool]:
    """Determine the largest odd number among the provided values."""
    # This function's job is to determine the largest odd number among
    # the provided three input values called first, second, and third.
    # If none of the numbers are odd, then determine the smallest of
    # the three values. There are multiple correct solutions.
    # TODO: implement the body of the function.
    # Ultimately, make sure that the function returns two values in the
    # form (answer, found_odd), fitting the function's signature.

    # You must use this exact line of code somewhere in the function
    # Call the get_minimum function to determine the smallest number
    answer = get_minimum(first, second, third)
    
    # TODO: Correct the placeholder return below
    return (0, False)
    

def parse_file(file_name: Path) -> List[List[int]]:
    # TODO: initialize the list of lists to be returned

    # TODO: if the file is valid:

        # TODO: get the file contents

        # TODO: split the file contents into lines

        # TODO: get access to each line one at a time:

            # TODO: split individual line to a list using comma delimiter

            # TODO: convert everything in the list into a integer


            # TODO: add the now int-converted list to the list to be returned

        # TODO: return the to-be-returned list 

    # TODO: raise an error if the file is not found


@cli.command()
def compare(
    first: int = typer.Option(0),
    second: int = typer.Option(0),
    third: int = typer.Option(0),
    input_file: Path = typer.Option(None),
) -> None:
    """Perform number comparison to find the largest odd number."""
    
    # TODO: create a console for rich text output - reference

    if input_file:
        try:
            (first, second, third) = parse_file(input_file)[0]
        except FileNotFoundError:
            console.print(f"{input_file} was not found")
            return

    # TODO: create program output that exactly matches the expected
    # output on the ProactiveProgrammers web site! You can search
    # for the name of this project which is called "Number Comparison"
