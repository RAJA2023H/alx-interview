#!/usr/bin/python3
"""N Queens puzzle solution"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
            range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nqueens(board, col, n):
    """
    Solve N Queens problem using Backtracking
    """
    # Base case: If all queens are placed, return True
    if col >= n:
        add_solution(board, n)
        return True
    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # Recur to place rest of the queens
            res = solve_nqueens(board, col + 1, n) or res
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0
    return res
def add_solution(board, n):
    """
    Add the solution to the final list
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)
def create_board(n):
    """
    Create an n x n sized chessboard with 0's
    """
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    return board
def main():
    """
    Main function to solve N Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = create_board(n)
    solve_nqueens(board, 0, n)
if __name__ == "__main__":
    main()
