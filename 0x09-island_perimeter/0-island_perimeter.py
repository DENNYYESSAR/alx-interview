#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island
in a grid representation. The island is represented by 1's (land), and
water is represented by 0's. The function calculates the perimeter of
the island by examining adjacent cells.
"""

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]): A list of lists where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island in the grid.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
