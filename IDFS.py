from TilePuzzleLogic import backtracking

class IDFS(object):

    def __init__(self, logic):
        self._logic = logic
        self._visited = 1

    def dfs_l(self, init_state, iteration=0, max_iteration=1):
        import copy

        current = copy.copy(init_state)
        self._visited += 1

        if self._logic.is_goal_state(current):
            # TODO: check the second return value in IDFS
            return backtracking(current), str(self._visited), str(iteration)

        if iteration == max_iteration:
            return None

        for son_state in self._logic.next_states(current):
            solution = self.dfs_l(son_state, iteration + 1, max_iteration)
            if solution is not None:
                    return solution

        # return none to show there is no result with this iteration limit
        return None

    def search(self, init_state):

        max_iteration, result = 1, None

        while not result:
            self._visited = 0
            result = self.dfs_l(init_state, 1, max_iteration)
            max_iteration += 1

        return result
