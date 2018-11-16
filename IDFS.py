from TilePuzzleLogic import backtracking


class IDFS(object):
    """
        IDFS using to search node by node deeply in a given graph.
        The search method using the logic given in the constructor.
    """

    def __init__(self, logic):
        self._logic = logic
        self._visited = 0

    def __dfs_l(self, init_state, iteration=0, max_iteration=1):
        """
        Search the given state with the current logic in order to find path for the goal.
        The search will only do max_max_iteration - iterations. If there is no solution return None.
        :param init_state: The state we are in.
        :param iteration: The current iteration.
        :param max_iteration: The Limit of the iterations.
        :return: The solution ,if existed.
        """
        import copy

        current = copy.copy(init_state)

        self._visited += 1

        if self._logic.is_goal_state(current):
            return backtracking(current), str(self._visited), str(iteration)

        if iteration == max_iteration:
            return None

        for son_state in self._logic.next_states(current):
            solution = self.__dfs_l(son_state, iteration + 1, max_iteration)
            if solution is not None:
                return solution

        # return none to show there is no result with this iteration limit
        return None

    def search(self, init_state):
        """
        The IDS search, using DFS-L algorithm.
        :param init_state: The state of the puzzle.
        :return: The solution if any.
        """
        max_iteration, result = 0, None

        while not result:
            self._visited = 0
            result = self.__dfs_l(init_state, 0, max_iteration)
            max_iteration += 1

        return result
