class Board(object):
    """
    Representing the board of the tile puzzle in order to optimized unwanted searching for
    space position.
    """
    def __init__(self, array=None,space=None,board=None):
        if board is None:
            # normal constructor
            self._array = array
            self._space = space
        else:
            # copy constructor
            self._space = board.space
            self._array = board.array

    def __copy__(self):
        """
        Simple copy method.
        :return: The copied board.
        """
        import copy
        copy_array = [copy.copy(row) for row in self._array]
        copy_space = self._space.copy()
        return Board(array=copy_array, space=copy_space)

    def __hash__(self):
        return hash(str(self._array))

    def __eq__(self, other):
        return self._array == other.array

    @property
    def array(self):
        return self._array

    @property
    def space(self):
        return self._space

    def get_element(self, i, j):
        return self._array[i][j]

    def find_space(self):
        """
        Find the space position in board, need to be called only once.
        :return: None.
        """
        for i, row in enumerate(self._array):
            for j, element in enumerate(row):
                if element == 0:
                    self._space = [i, j]
                    return

    def swap(self, num_pos):
        """
        Swap space tile with num_pos, also update new space tile.
        :param num_pos: A given Tile to swap.
        :return: None.
        """
        space_i, space_j = self._space[0], self._space[1]
        num_i, num_j = num_pos[0], num_pos[1]

        # swap the numbered tile with the space tile
        self._array[space_i][space_j], self._array[num_i][num_j] = self._array[num_i][num_j], self._array[space_i][space_j]
        # update space location
        self._space = num_pos