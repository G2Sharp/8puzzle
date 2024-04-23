class EightPuzzle:
    def __init__(self, initial_state):
        self.size = len(initial_state)
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimentos possíveis: direita, esquerda, baixo, cima
        self.empty_tile = self.find_empty_tile(initial_state)

    def find_empty_tile(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return (i, j)

    def move(self, state, action):
        new_state = [row[:] for row in state]  # Criar uma cópia do estado atual
        empty_row, empty_col = self.empty_tile
        new_row, new_col = empty_row + action[0], empty_col + action[1]
        if 0 <= new_row < self.size and 0 <= new_col < self.size:
            # Trocar a peça vazia com a peça na nova posição
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            return new_state, (new_row, new_col)
        return None, None
    
    def move_up(self):
        empty_row, empty_col = self.empty_tile
        if empty_row > 0:
            self.initial_state[empty_row][empty_col], self.initial_state[empty_row - 1][empty_col] = self.initial_state[empty_row - 1][empty_col], self.initial_state[empty_row][empty_col]
            self.empty_tile = (empty_row - 1, empty_col)
            print(self.initial_state)

    def move_down(self):
        empty_row, empty_col = self.empty_tile
        if empty_row < self.size - 1:
            self.initial_state[empty_row][empty_col], self.initial_state[empty_row + 1][empty_col] = self.initial_state[empty_row + 1][empty_col], self.initial_state[empty_row][empty_col]
            self.empty_tile = (empty_row + 1, empty_col)
            print(self.initial_state)


    def move_left(self):
        empty_row, empty_col = self.empty_tile
        if empty_col > 0:
            self.initial_state[empty_row][empty_col], self.initial_state[empty_row][empty_col - 1] = self.initial_state[empty_row][empty_col - 1], self.initial_state[empty_row][empty_col]
            self.empty_tile = (empty_row, empty_col - 1)
            print(self.initial_state)


    def move_right(self):
        empty_row, empty_col = self.empty_tile
        if empty_col < self.size - 1:
            self.initial_state[empty_row][empty_col], self.initial_state[empty_row][empty_col + 1] = self.initial_state[empty_row][empty_col + 1], self.initial_state[empty_row][empty_col]
            self.empty_tile = (empty_row, empty_col + 1)
            print(self.initial_state)

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_possible_moves(self, state):
        moves = []
        for action in self.actions:
            new_state, _ = self.move(state, action)
            if new_state:
                moves.append(new_state)
        return moves
    
    def goal_position(self, value):
        for i in range(self.size):
            for j in range(self.size):
                if self.goal_state[i][j] == value:
                    return i, j
