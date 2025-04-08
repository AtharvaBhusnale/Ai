def board_position(n):
    board = [-1] * n
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print(f"\nTotal solutions found: {len(solutions)}")
    
    for index, sol in enumerate(solutions, start=1):
        print(f"\nSolution {index}:")
        print_solution_matrix(sol, n)

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())  # Save current valid configuration
        return
    
    for col in range(n):
        if safe_position(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def safe_position(board, row, col):
    for i in range(row):
        if (board[i] == col or 
            absolute_value(board[i] - col) == absolute_value(i - row)):
            return False
    return True

def absolute_value(x):
    return x if x >= 0 else -x

def print_solution_matrix(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
        
num=int(input("Enter the size of matrix"))
board_position(num)
