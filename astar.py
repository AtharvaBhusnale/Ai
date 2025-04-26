import heapq

# Goal state as a tuple
goal = (1,2,3,4,5,6,7,8,0)

# Moves: up, down, left, right
moves = {
    0: [1, 3],
    1: [0,2,4],
    2: [1,5],
    3: [0,4,6],
    4: [1,3,5,7],
    5: [2,4,8],
    6: [3,7],
    7: [4,6,8],
    8: [5,7]
}

def heuristic(state):
    """Manhattan distance"""
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            goal_pos = goal.index(value)
            distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

def a_star(start):
    heap = []
    heapq.heappush(heap, (heuristic(start), 0, start, []))  # (priority, cost, state, path)
    visited = set()

    while heap:
        priority, cost, state, path = heapq.heappop(heap)

        if state == goal:
            return path + [state]

        visited.add(state)

        zero = state.index(0)
        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                heapq.heappush(heap, (cost + 1 + heuristic(new_state), cost + 1, new_state, path + [state]))

    return None

# Example
start = (1,2,3,4,0,6,7,5,8)

solution = a_star(start)

if solution:
    print("Steps to solve:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found.")
