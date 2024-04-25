class EightPuzzleSolver:
    def __init__(self, puzzle):
        # Inicializa o solver com o quebra-cabeça fornecido
        self.puzzle = puzzle
        self.counter = 0  # Contador de movimentos

    def bfs(self):
        # Busca em Largura (BFS) para resolver o quebra-cabeça
        self.counter = 0
        initial_state = self.puzzle.initial_state
        if self.puzzle.is_goal_state(initial_state):
            return initial_state
        frontier = [initial_state]  # Fronteira inicial com o estado inicial
        explored = set()  # Conjunto de estados explorados
        while frontier:
            current_state = frontier.pop(0)  # Remove o primeiro estado da fronteira
            explored.add(
                tuple(map(tuple, current_state))
            )  # Adiciona o estado atual aos explorados
            if self.puzzle.is_goal_state(current_state):
                return self._report(
                    "BFS", current_state
                )  # Retorna a solução encontrada
            for move in self.puzzle.get_possible_moves(current_state):
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    explored.add(move_tuple)
                    frontier.append(
                        move
                    )  # Adiciona os próximos estados possíveis à fronteira
                    self._print_move("BFS", move)
        return None

    def dfs(self):
        # Busca em Profundidade (DFS) para resolver o quebra-cabeça
        self.counter = 0
        initial_state = self.puzzle.initial_state
        if self.puzzle.is_goal_state(initial_state):
            return initial_state
        frontier = [initial_state]  # Fronteira inicial com o estado inicial
        explored = set()  # Conjunto de estados explorados
        while frontier:
            current_state = frontier.pop()  # Remove o último estado da fronteira
            explored.add(
                tuple(map(tuple, current_state))
            )  # Adiciona o estado atual aos explorados
            if self.puzzle.is_goal_state(current_state):
                return self._report(
                    "DFS", current_state
                )  # Retorna a solução encontrada
            for move in self.puzzle.get_possible_moves(current_state):
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    frontier.append(
                        move
                    )  # Adiciona os próximos estados possíveis à fronteira
                    self._print_move("DFS", move)
        return None

    def gbfs(self, type):
        # Busca Gulosa (GBFS) para resolver o quebra-cabeça
        self.counter = 0
        initial_state = self.puzzle.initial_state
        if self.puzzle.is_goal_state(initial_state):
            return initial_state
        frontier = [
            (self.heuristic(initial_state, type), initial_state)
        ]  # Fronteira com a heurística de Manhattan
        explored = set()  # Conjunto de estados explorados
        while frontier:
            _, current_state = frontier.pop(
                0
            )  # Remove o estado com menor heurística da fronteira
            explored.add(
                tuple(map(tuple, current_state))
            )  # Adiciona o estado atual aos explorados
            if self.puzzle.is_goal_state(current_state):
                return self._report(
                    "GBFS", current_state
                )  # Retorna a solução encontrada
            for move in self.puzzle.get_possible_moves(current_state):
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in explored:
                    explored.add(move_tuple)
                    heuristic_value = self.heuristic(
                        move, type
                    )  # Calcula a heurística de Manhattan para o próximo estado
                    frontier.append(
                        (heuristic_value, move)
                    )  # Adiciona os próximos estados possíveis à fronteira com sua heurística
                    frontier.sort(
                        key=lambda x: x[0]
                    )  # Ordena a fronteira com base na heurística
                    self._print_move_h("GBFS", type, move)

        return None

    def heuristic(self, state, t):
        # Calcula a heurística para um estado dado
        distance = 0
        if t == "MDH":
            # Heurística da Distância de Manhattan
            for i in range(self.puzzle.size):
                for j in range(self.puzzle.size):
                    if state[i][j] != 0:
                        goal_row, goal_col = self.puzzle.goal_position(state[i][j])
                        distance += abs(i - goal_row) + abs(j - goal_col)
        else:
            # Heurística da Distância de Hamming
            for i in range(self.puzzle.size):
                for j in range(self.puzzle.size):
                    if state[i][j] != self.puzzle.goal_state[i][j]:
                        distance += 1
        return distance

    def _report(self, algorithm, solution):
        # Reporta a solução encontrada pelo algoritmo
        print(f"---------------{algorithm}-Report-----------------")
        print(f"Total moves: {self.counter}")
        print("Solution found:", solution)
        print(f"---------------{algorithm}-Report-----------------")
        return solution

    def _print_move(self, algorithm, move):
        # Imprime o movimento realizado pelo algoritmo
        print(f"Move ~> {self.counter} | {algorithm} | {move}")
        self.counter += 1

    def _print_move_h(self, algorithm, t, move):
        # Imprime o movimento realizado pelo algoritmo
        if algorithm == "GBFS" and t == "MDH":
            print(f"Move ~> {self.counter} | {algorithm} | {t} | {move}")
        else:
            t = "HH"
            print(f"Move ~> {self.counter} | {algorithm} | {t} | {move}")
        self.counter += 1
