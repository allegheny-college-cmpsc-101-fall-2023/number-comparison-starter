"""Perform number comparison to find the largest odd number."""

# TODO: make sure that you resolve all of the TODO markers inside
# of this file. Once you are done with a TODO marker you should
# either delete it and rewrite the comment or delete the entire comment

from typing import Tuple

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
    # the three values.
    # TODO: implement the body of the function.
    # Ultimately, make sure that the function returns two values in the
    # form (answer, found_odd), fitting the function's signature.
    # Be able to answer to yourself, what is the type of "found_odd"
    # Think about "found_odd" as answering: did your algorithm find the 
    # the largest odd number among the three inputs?

    # You must use this exact line of code somewhere in the function
    # Call the get_minimum function to determine the smallest number
    answer = get_minimum(first, second, third)
    
    # The return below is a placeholder
    return (0, False)


@cli.command()
def compare(
    first: int = typer.Option(...),
    second: int = typer.Option(...),
    third: int = typer.Option(...),
) -> None:
    """Perform number comparison to find the largest odd number."""
    # TODO: create a console for rich text output - reference
    # ^^^ for this TODO, reference Integer Square and Primality.

    # TODO: create program output that exactly matches the expected
    # output on the ProactiveProgrammers web site! You can search
    # for the name of this project which is called "Number Comparison"
    # ^^^ for this TODO, think about what information needs to be
    # known or checked before you can print out all the
    # necessary messages. Be able to answer to yourself, what functions
    # will let me get this information.
