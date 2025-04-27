# Pretty print the 8-puzzle matrix
def print_puzzle(state, level, heuristic):
    print(f"\n------ Level {level} ------")
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print(f"Heuristic (Misplaced Tiles): {heuristic}")

# Heuristic: Count misplaced tiles
def misplaced_tiles(state):
    goal = [1, 2, 3, 8,0, 4, 7, 6, 5]       
    count = 0
    for i in range(9):
        # Only count if tile is non-zero and in wrong position
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

# Find best move based on heuristic
def best_move(state, visited):
    zero = state.index(0)
    move_map = {
        0: [1,3], 1: [0,2,4], 2: [1,5],
        3: [0,4,6], 4: [1,3,5,7], 5: [2,4,8],
        6: [3,7], 7: [4,6,8], 8: [5,7]
    }
    best = None     #best state to move to
    best_h = float('inf') #best heuristic value

    for move in move_map[zero]:
        new_state = state.copy()
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        if tuple(new_state) in visited:
            continue
        h = misplaced_tiles(new_state)
        if h < best_h:
            best, best_h = new_state, h

    return best, best_h

# -------- Main Program --------
initial = [2,8,3,1,6,4,7,0,5]  # Initial state of the puzzle
state = initial
visited = {tuple(state)}
level = 0
heuristic = misplaced_tiles(state)

print_puzzle(state, level, heuristic)

while heuristic > 0:
    next_state, next_h = best_move(state, visited)
    if not next_state:
        print("\n❌ No better move found. Stuck at local minimum!")
        break
    level += 1
    state = next_state
    heuristic = next_h
    visited.add(tuple(state))
    print_puzzle(state, level, heuristic)
