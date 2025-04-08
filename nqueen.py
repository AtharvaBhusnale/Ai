def board_position(n):
    board = [-1] * n  # Initialize the board with -1 (no queen placed)
    solutions = []    # List to store all valid solutions
    solve_n_queens(board, 0, n, solutions)  # Start from row 0
    print(f"\nTotal solutions found: {len(solutions)}")
    
    # Print each solution in matrix form
    for index, sol in enumerate(solutions, start=1):
        print(f"\nSolution {index}:")
        print_solution_matrix(sol, n)

# Recursive backtracking function to solve N-Queens
def solve_n_queens(board, row, n, solutions):
    if row == n:
        # All queens placed successfully, save the board configuration
        solutions.append(board.copy())
        return
    
    # Try placing a queen in every column of the current row
    for col in range(n):
        if safe_position(board, row, col):  # Check if position is safe
            board[row] = col  # Place queen
            solve_n_queens(board, row + 1, n, solutions)  # Recurse for next row
            board[row] = -1  # Backtrack: remove the queen

# Check whether placing a queen at (row, col) is safe
def safe_position(board, row, col):
    for i in range(row):
        # Check if same column or same diagonal
        if (board[i] == col or absolute_value(board[i] - col) == absolute_value(i - row)):
            return False  # Conflict with another queen
    return True  # Safe to place

# Helper function to get absolute value (like abs())
def absolute_value(x):
    return x if x >= 0 else -x

# Print the board in a matrix form using 'Q' for queens and '.' for empty spots
def print_solution_matrix(solution, n):
    for row in range(n):
        for col in range(n):
            if solution[row]==col :
               print("Q ",end=" ")
            else :
                print(". ",end=" ")

        print(" ")
# Run the function for 8x8 board
board_position(8)
