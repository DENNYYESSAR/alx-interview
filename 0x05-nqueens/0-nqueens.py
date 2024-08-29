#!/usr/bin/python3
"""
N Queens Puzzle Solver

This script solves the N Queens problem, which involves placing N
non-attacking queens on an N×N chessboard. The program prints all possible
solutions to the problem.

Usage:
    nqueens N

Where:
    N is an integer greater than or equal to 4.
"""

import sys
from typing import List, Tuple


def print_usage_and_exit():
    """Prints the usage message and exits the program."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input(args: List[str]) -> int:
    """
    Validates the command line input arguments.

    Args:
        args (List[str]): Command line arguments.

    Returns:
        int: The valid integer N for the N queens problem.

    Raises:
        SystemExit: If the input is invalid.
    """
    if len(args) != 2:
        print_usage_and_exit()

    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve_nqueens(n: int) -> List[List[Tuple[int, int]]]:
    """
    Solves the N Queens problem.

    Args:
        n (int): The size of the chessboard (N×N).

    Returns:
        List[List[Tuple[int, int]]]: A list of solutions, where each solution
        is a list of tuples representing the coordinates of the queens.
    """
    solutions = []
    solve_recursive(0, [], solutions, n)
    return solutions


def solve_recursive(row, current_solution, solutions, n):
    if row == n:
        solutions.append(current_solution.copy())
        return

    for col in range(n):
        if is_safe(row, col, current_solution):
            current_solution.append((row, col))
            solve_recursive(row + 1, current_solution, solutions, n)
            current_solution.pop()


def is_safe(row, col, current_solution):
    """
    Checks if placing a queen at the given row and column is safe.

    Args:
        row (int): The row index.
        col (int): The column index.
        current_solution (List[Tuple[int, int]]): The current list of queen
        positions.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for r, c in current_solution:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def print_solutions(solutions: List[List[Tuple[int, int]]]) -> None:
    """
    Prints the solutions to the N Queens problem.

    Args:
        solutions (List[List[Tuple[int, int]]]): A list of solutions.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    n = validate_input(sys.argv)
    solutions = solve_nqueens(n)
    print_solutions(solutions)
