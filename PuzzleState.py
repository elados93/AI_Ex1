class State(object):

    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            # normal constructor
            self._board = board
            self._move = move
            self.came_from = came_from
        else:
            # copy constructor
            self._board = state.board
            self._move = state.move
            self.came_from = state.came_from

    def __copy__(self):
        import copy

        copy_board = copy.copy(self._board)
        return State(board=copy_board,move=self._move, came_from=self.came_from)

    def __hash__(self):
        return hash(self._board)

    @property
    def board(self):
        return self._board

    @property
    def move(self):
        return self._move

    def __eq__(self, other):
        return self._board == other.board

class HeuristicState(State):

    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            # constructor using other parameters
            State.__init__(self, board, move, came_from)
        else:
            # constructor using a given state
            State.__init__(self,state=state)
        self.h_cost = 0
        self.g_cost = 0

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    @property
    def f_cost(self):
        return self.h_cost + self.g_cost
