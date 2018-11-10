from PuzzleState import State

space_rep = '0'


class TilePuzzleLogic(object):
    def __init__(self, n):
        self._n = n

    @property
    def n(self):
        return self._n

    def next_states(self, state):

        ans = []
        board = state.board
        space_pos = self.find_space(board)

        up_pos = (space_pos[0] - 1, space_pos[1])
        down_pos = (space_pos[0] + 1, space_pos[1])
        left_pos = (space_pos[0], space_pos[1] - 1)
        right_pos = (space_pos[0], space_pos[1] + 1)

        # up position
        if state.move != 'U' and self.is_valid(up_pos):
            up_board = [row.copy() for row in board]
            TilePuzzleLogic.swap(up_board, space_pos, up_pos)
            ans.append(State(up_board, came_from=state, move='D'))

        # left position
        if state.move != 'L' and self.is_valid(left_pos):
            left_board = [row.copy() for row in board]
            TilePuzzleLogic.swap(left_board, space_pos, left_pos)
            ans.append(State(left_board, came_from=state, move='R'))

        # down position
        if state.move != 'D' and self.is_valid(down_pos):
            down_board = [row.copy() for row in board]
            TilePuzzleLogic.swap(down_board, space_pos, down_pos)
            ans.append(State(down_board, came_from=state, move='U'))

        # right position
        if state.move != 'R' and self.is_valid(right_pos):
            right_board = [row.copy() for row in board]
            TilePuzzleLogic.swap(right_board, space_pos, right_pos)
            ans.append(State(right_board, came_from=state, move='L'))

        return ans

    def find_space(self, board):
        """
        The function will return the space position in board as a tuple.
        :param board: The board of the Tile Puzzle.
        :return: Tuple (i, j) represent the space position.
        """

        for row in range(self._n):
            for col in range(self._n):
                if board[row][col] == space_rep:
                    return row, col

        return -1, -1

    def is_valid(self, pos):
        """
        Return True/False if the position is valid on grid.
        :param pos: Position to check.
        :return: True/False if pos is valid on board.
        """
        return 0 <= pos[0] < self._n and 0 <= pos[1] < self._n

    def calc_heuristic(self, state):
        h = 0
        board = state.board

        for i in range(self._n):
            for j in range(self._n):

                if board[i][j] != space_rep:
                    tile_as_number = int(board[i][j])
                    correct_x = (tile_as_number - 1) // self._n
                    correct_y = (tile_as_number - 1) % self._n
                else:
                    continue
                h += calc_diffs(i, j, correct_x, correct_y)

        return h

    # TODO: add this function
    # def calc_son_heuristic(self, son_state):
    #     father_node = son_state.came_from
    #     move = son_state.move

    @staticmethod
    def swap(board, space_pos, num_pos):
        space_i, space_j = space_pos[0], space_pos[1]
        num_i, num_j = num_pos[0], num_pos[1]

        board[space_i][space_j], board[num_i][num_j] = board[num_i][num_j], board[space_i][space_j]

    @staticmethod
    def is_goal_state(state):
        board = state.board
        counter = 1

        for row in board:
            for elem in row:
                if elem != space_rep and elem != str(counter):
                    return False
                counter += 1

        return True


def backtracking(goal):
    path = []
    current = goal
    while current.came_from:
        path.insert(0, current.move)
        current = current.came_from
    return ''.join(path)


def calc_diffs(i, j, correct_x, correct_y):
    return abs(i - correct_x) + abs(j - correct_y)
