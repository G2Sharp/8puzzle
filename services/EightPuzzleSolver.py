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
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    explored.add(move_tuple)
                    frontier.append(move)
                    print("Move",move)

        return None  # Se não encontrar a solução

    def dfs(self):
        initial_state = self.puzzle.initial_state

        if self.puzzle.is_goal_state(initial_state):
            return initial_state

        frontier = [initial_state]
        explored = set()

        while frontier:
            current_state= frontier.pop()
            explored.add(tuple(map(tuple, current_state)))

            if self.puzzle.is_goal_state(current_state):
                return current_state

            for move in self.puzzle.get_possible_moves(current_state):
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    frontier.append((move))
                    print("Move",move)


        return None  # If solution not found
    

    
    def gbfs(self):
        initial_state = self.puzzle.initial_state

        if self.puzzle.is_goal_state(initial_state):
            return initial_state

        frontier = [(self.hamming_heuristic(initial_state), initial_state)]  # Priority queue based on heuristic value
        explored = set()

        while frontier:
            _, current_state = frontier.pop(0)  # Pop the state with the lowest heuristic value
            explored.add(tuple(map(tuple, current_state)))  # Convert nested list to tuple for hashability

            if self.puzzle.is_goal_state(current_state):
                return current_state

            for move in self.puzzle.get_possible_moves(current_state):
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    explored.add(move_tuple)
                    frontier.append((self.hamming_heuristic(move), move))
                    frontier.sort(key=lambda x: x[0])  # Sort frontier based on heuristic value
                    print("Move",move)


        return None  # If solution not found

    def manhattan_distance_heuristic(self, state):
        # Manhattan distance heuristic
        distance = 0
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                if state[i][j] != 0:  # Skip empty tile
                    goal_row, goal_col = self.puzzle.goal_position(state[i][j])
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance
    
    def hamming_heuristic(self, state):
        # Hamming distance heuristic
        distance = 0
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                if state[i][j] != self.puzzle.goal_state[i][j]:  # Check if tile is in correct position
                    distance += 1
        return distance
