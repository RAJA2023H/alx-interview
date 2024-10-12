#!/usr/bin/python3
"""
defines method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    doc
    """

    n = len(boxes)
    opened = set([0])  # Set of opened boxes, data structure"""
    stack = [0]  # initialize the stack with [0]"""

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in opened:
                opened.add(key)
                stack.append(key)
    return len(opened) == n  # debug"""
