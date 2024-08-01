#!/usr/bin/python3
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determine if all boxes can be opened."""

    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # Box 0 is unlocked initially

    stack = [0]  # Start with box 0

    while stack:
        current_box = stack.pop()
        # Iterate over keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
