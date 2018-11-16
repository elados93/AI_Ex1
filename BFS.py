from TilePuzzleLogic import backtracking

class BFS_Seaerch(object):
    """
        BFS_Seaerch using to search level by level in a given graph.
        The search method using the logic given in the constructor.
    """

    def __init__(self, logic):
        self._logic = logic

    def search(self, init_state):
        """
        Search the given state with the current logic in order to find path for the goal.
        :param init_state: The state of the puzzle.
        :return: Tuple of: path of operators, the number of states we visited, 0.
        """
        open_list = []
        count = 0

        open_list.append(init_state)

        while len(open_list):
            current = open_list.pop(0)

            # count all the states we popped from the queue
            count += 1

            if self._logic.is_goal_state(current):
                return backtracking(current), str(count), '0'

            children = self._logic.next_states(current)

            for child in children:
                open_list.append(child)

        # BFS is complete, but if there is no answer raise an exception.
        raise Exception('Puzzle is not solvable!')
