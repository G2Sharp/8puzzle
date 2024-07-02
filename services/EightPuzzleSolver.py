from collections import deque
import heapq


# BFS
def bfs(puzzle):
    initial_state = puzzle.initial_state
    frontier = deque([(initial_state, [])])
    explored = set()

    while frontier:
        state, path = frontier.popleft()

        if puzzle.is_goal_state(state):
            print("BFS Solution Found:")
            print("Path Length:", len(path))
            for i, move in enumerate(path):
                print(f"Move {i + 1}:")
                puzzle.print_state(move)
            print("Goal State:")
            puzzle.print_state(state)
            return path + [state]

        explored.add(state)

        for neighbor in puzzle.get_possible_moves(state):
            if neighbor not in explored and all(
                neighbor != item[0] for item, _ in frontier
            ):
                frontier.append((neighbor, path + [state]))

    return None


# DFS
def dfs(puzzle):
    initial_state = puzzle.initial_state
    frontier = [(initial_state, [])]
    explored = set()

    while frontier:
        state, path = frontier.pop()

        if puzzle.is_goal_state(state):
            print("DFS Solution Found:")
            print("Path Length:", len(path))
            for i, move in enumerate(path):
                print(f"Move {i + 1}:")
                puzzle.print_state(move)
            print("Goal State:")
            puzzle.print_state(state)
            return path + [state]

        explored.add(state)

        for neighbor in puzzle.get_possible_moves(state):
            if neighbor not in explored and all(
                neighbor != item[0] for item, _ in frontier
            ):
                frontier.append((neighbor, path + [state]))

    return None


# Greedy Search
def heuristic(state, goal_state, type):
    # Usando a soma das distâncias de Manhattan como heurística
    if type.lower() == "mhd":
        distance = 0
        goal_positions = {goal_state[i][j]: (i, j) for i in range(3) for j in range(3)}

        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i, goal_j = goal_positions[state[i][j]]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    # Usando a soma das distâncias de Hamming como heurística
    else:
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                    distance += 1  # Conta o número de tiles fora de lugar
        return distance


def greedy_search(puzzle, type):
    initial_state = puzzle.initial_state
    goal_state = puzzle.goal_state
    frontier = []
    heapq.heappush(
        frontier, (heuristic(initial_state, goal_state, type), initial_state, [])
    )
    explored = set()

    while frontier:
        _, state, path = heapq.heappop(frontier)

        if puzzle.is_goal_state(state):
            print("Greedy Search Solution Found:")
            print("Path Length:", len(path))
            print(
                "Heuristc:",
                "Manhatan Distance" if type.lower() == "mhd" else "Hamming Distance",
            )
            for i, move in enumerate(path):
                print(f"Move {i + 1}:")
                puzzle.print_state(move)
            print("Goal State:")
            puzzle.print_state(state)
            return path + [state]

        explored.add(state)

        for neighbor in puzzle.get_possible_moves(state):
            if neighbor not in explored and all(
                neighbor != item[1] for _, item, _ in frontier
            ):
                heapq.heappush(
                    frontier,
                    (heuristic(neighbor, goal_state, type), neighbor, path + [state]),
                )

    return None
