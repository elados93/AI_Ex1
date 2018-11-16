from PuzzleState import State
from Board import Board

# number that represent the space tile
space_rep = 0

class TilePuzzleLogic(object):
    """
    The logic of the tile puzzle. Contains the heuristic function and goal function in order
    to check if a given state is a goal state. Also has the method for the successor's states
    """

    def __init__(self, n):
        self._n = n
        self._solved_board = None
        self.__generate_goal_board()

    def __generate_goal_board(self):
        """
        The method creates the goal state and stores it in the class.
        :return: None.
        """
        element = 1
        array = []

        for row in range(self._n):
            row_to_append = []
            for col in range(self._n):
                row_to_append.append(element)
                element += 1
            array.append(row_to_append)

        array[self._n - 1][self._n - 1] = 0
        self._solved_board = Board(array=array, space=[self._n - 1, self._n - 1])

    @property
    def n(self):
        return self._n

    def next_states(self, state):
        """
        Return a list of the successors states of a given state.
        :param state: A given state
        :return: The successors.
        """
        import copy

        ans = []
        current_array = state.board.array
        space_pos = state.board.space

        up_pos = [space_pos[0] - 1, space_pos[1]]
        down_pos = [space_pos[0] + 1, space_pos[1]]
        left_pos = [space_pos[0], space_pos[1] - 1]
        right_pos = [space_pos[0], space_pos[1] + 1]

        # down position
        if self.__is_valid(down_pos):
            down_array = [copy.copy(row) for row in current_array]
            down_board = Board(array=down_array, space=space_pos.copy())
            down_board.swap(down_pos)
            ans.append(State(board=down_board, came_from=state, move='U'))

        # up position
        if self.__is_valid(up_pos):
            up_array = [copy.copy(row) for row in current_array]
            up_board = Board(array=up_array, space=space_pos.copy())
            up_board.swap(up_pos)
            ans.append(State(board=up_board, came_from=state, move='D'))

        # right position
        if self.__is_valid(right_pos):
            right_array = [copy.copy(row) for row in current_array]
            right_board = Board(array=right_array, space=space_pos.copy())
            right_board.swap(right_pos)
            ans.append(State(board=right_board, came_from=state, move='L'))

        # left position
        if self.__is_valid(left_pos):
            left_array = [copy.copy(row) for row in current_array]
            left_board = Board(array=left_array, space=space_pos.copy())
            left_board.swap(left_pos)
            ans.append(State(board=left_board, came_from=state, move='R'))

        return ans

    def __is_valid(self, pos):
        """
        Return True/False if the position is valid on grid.
        :param pos: Position to check.
        :return: True/False if pos is valid on board.
        """
        return 0 <= pos[0] < self._n and 0 <= pos[1] < self._n

    def calc_heuristic(self, state):
        """
        Calc the heuristic of a given state using manhattan distance.
        :param state: State to calc heuristic for.
        :return: The heuristic value of state.
        """
        h = 0
        board = state.board.array

        for i in range(self._n):
            for j in range(self._n):

                if board[i][j] != space_rep:
                    tile_as_number = board[i][j]
                    correct_x = (tile_as_number - 1) // self._n
                    correct_y = (tile_as_number - 1) % self._n
                else:
                    continue
                h += calc_diffs(i, j, correct_x, correct_y)
        return h

    def calc_son_heuristic(self, son_state):
        """
        Optimization for calculating heuristic for son_state quickly.
        :param son_state: The son state to calc h_val.
        :return: The h_val of son_state.
        """
        father_node = son_state.came_from

        if father_node is None:
            return self.calc_heuristic(son_state)

        move = son_state.move

        father_node_space = father_node.board.space.copy()
        element_to_swap = son_state.board.get_element(father_node_space[0], father_node_space[1])
        correct_x, correct_y = (element_to_swap - 1) // self._n, (element_to_swap - 1) % self._n
        after_swap_moves = calc_diffs(father_node_space[0], father_node_space[1], correct_x, correct_y)

        if move == 'L':
            father_node_space[1] += 1
        elif move == 'R':
            father_node_space[1] -=1
        elif move == 'U':
            father_node_space[0] += 1
        else:
            father_node_space[0] -= 1

        before_swap_moves = calc_diffs(father_node_space[0], father_node_space[1], correct_x, correct_y)

        return father_node.h_cost + (after_swap_moves - before_swap_moves)

    def is_goal_state(self, state):
        """
        True or false if state is goal state.
        :param state: The state to inspect.
        :return: True or false if it's a goal state.
        """
        return self._solved_board == state.board

def backtracking(goal):
    """
    Given the goal state construct the path to it from init state.
    :param goal: The goal we found.
    :return: The path to the goal.
    """
    path = []
    current = goal
    while current.came_from:
        path.insert(0, current.move)
        current = current.came_from
    return ''.join(path)


def calc_diffs(i, j, correct_x, correct_y):
    """
    Calc the manhattan distance between 2 coordinates.
    :param i: Trivial.
    :param j: Trivial.
    :param correct_x: Trivial.
    :param correct_y: Trivial.
    :return: The distance.
    """
    return abs(i - correct_x) + abs(j - correct_y)
