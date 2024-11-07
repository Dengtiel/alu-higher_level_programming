#!/usr/bin/python3
import sys


def print_solution(solution):
    """Prints the board configuration as required."""
    print([[row, col] for row, col in enumerate(solution)])


def is_safe(solution, row, col):
    """Checks if a queen can be placed at (row, col) without conflicts."""
    for i in range(row):
        if solution[i] == col or \
           solution[i] - i == col - row or \
           solution[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, solution=[]):
    """Uses backtracking to find all solutions to the N Queens problem."""
    if row == n:
        print_solution(solution)
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solve_nqueens(n, row + 1, solution + [col])


def main():
    """Main function to parse input and initiate the
    N Queens solution search."""
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
