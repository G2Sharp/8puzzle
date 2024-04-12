from collections import deque

class EightPuzzleSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def bfs(self):
        initial_state = self.puzzle.initial_state

        if self.puzzle.is_goal_state(initial_state):
            return initial_state

        frontier = deque([initial_state])
        explored = set()

        while frontier:
            current_state = frontier.popleft()
            explored.add(tuple(map(tuple, current_state)))


            if self.puzzle.is_goal_state(current_state):
                    return current_state
            for move in self.puzzle.get_possible_moves(current_state):
                if tuple(map(tuple, move)) not in explored:
                    explored.add(tuple(map(tuple, move)))
                    frontier.append(move)
                    print("Move",move)

        return None  # Se não encontrar a solução


