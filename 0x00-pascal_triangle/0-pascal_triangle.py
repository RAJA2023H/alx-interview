#!/usr/bin/python3
"""
Functions:
pascal_triangle: creates the mentioned triangle.

Usage:
    Import and use it.
"""
def pascal_triangle(n):
    """
    name: pascal_triangle
    Returns a Pascal Triangle
    Args:
        n: integer

    Returns:
        list: list of integers
    """
     triangle = []
    if rows > 0:
        triangle.append([1])
        for row in range(1, rows):
            current_row = []
            for col in range(row + 1):
                value = 0
                if col > 0:
                    value += triangle[row - 1][col - 1]
                if col < row:
                    value += triangle[row - 1][col]
                current_row.append(value)
            triangle.append(current_row)
    return triangle


if __name__ == "__main__":
    """
    Testing the Pascal's Triangle generation.
    """
    def display_triangle(triangle):
        for row in triangle:
            print(row)

    result = generate_pascal_triangle(5)
    display_triangle(result)
