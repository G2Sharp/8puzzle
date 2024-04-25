class EightPuzzle:
    def __init__(self, initial_state):
        # Tamanho do quebra-cabeça (n x n)
        self.size = len(initial_state)

        # Estado inicial do quebra-cabeça
        self.initial_state = initial_state

        # Estado objetivo do quebra-cabeça
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        # Lista de ações possíveis: direita, esquerda, baixo, cima
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Posição do tile/azulejo vazio
        self.empty_tile = self.find_empty_tile(initial_state)

    def find_empty_tile(self, state):
        # Encontra a posição do tile/azulejo vazio no estado fornecido
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return (i, j)

    def move(self, state, action):
        # Cria uma cópia do estado atual
        new_state = [row[:] for row in state]

        # Encontra a posição do tile/azulejo vazio
        empty_row, empty_col = self.empty_tile

        # Calcula a nova posição após o movimento
        new_row, new_col = empty_row + action[0], empty_col + action[1]

        # Verifica se a nova posição está dentro dos limites do quebra-cabeça
        if 0 <= new_row < self.size and 0 <= new_col < self.size:
            # Realiza o movimento trocando o tile/azulejo vazio pelo tile/azulejo na nova posição
            new_state[empty_row][empty_col], new_state[new_row][new_col] = (
                new_state[new_row][new_col],
                new_state[empty_row][empty_col],
            )

            # Retorna o novo estado e a posição do tile/azulejo vazio no novo estado
            return new_state, (new_row, new_col)

        # Retorna None se o movimento for inválido
        return None, None

    def is_goal_state(self, state):
        # Verifica se o estado fornecido é o estado objetivo
        return state == self.goal_state

    def get_possible_moves(self, state):
        # Retorna uma lista de estados possíveis após aplicar todas as ações possíveis
        moves = []
        for action in self.actions:
            new_state, _ = self.move(state, action)
            if new_state:
                moves.append(new_state)
        return moves

    def goal_position(self, value):
        # Encontra a posição do valor fornecido no estado objetivo
        for i in range(self.size):
            for j in range(self.size):
                if self.goal_state[i][j] == value:
                    return i, j
