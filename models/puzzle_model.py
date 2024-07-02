class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = tuple(map(tuple, initial_state))
        self.goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        self.size = 3
        self.actions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]  # Movimentos: Cima, Baixo, Esquerda, Direita

    def is_goal_state(self, state):
        return state == self.goal_state

    def find_empty_tile(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, action):
        empty_row, empty_col = self.find_empty_tile(state)
        new_row, new_col = empty_row + action[0], empty_col + action[1]

        if 0 <= new_row < self.size and 0 <= new_col < self.size:
            new_state = [list(row) for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = (
                new_state[new_row][new_col],
                new_state[empty_row][empty_col],
            )
            return tuple(map(tuple, new_state))

        return None

    def get_possible_moves(self, state):
        possible_moves = []
        for action in self.actions:
            new_state = self.move(state, action)
            if new_state:
                possible_moves.append(
                    new_state
                )  # Adiciona os movimentos possíveis à lista
        return possible_moves

    def print_state(self, state):
        for row in state:
            print(
                " ".join(str(tile) if tile != 0 else "_" for tile in row)
            )  # Imprime o estado do quebra-cabeça

    def print_move(self, before_state, after_state):
        print("\nBefore move:")
        self.print_state(before_state)  # Imprime o estado antes do movimento
        print("After move:")
        self.print_state(after_state)  # Imprime o estado após o movimento
        print(
            f"Inversion count remains {self.count_inversions(after_state)} after the move"
        )  # Conta as inversões
