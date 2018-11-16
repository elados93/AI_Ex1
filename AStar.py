from TilePuzzleLogic import backtracking
from PuzzleState import HeuristicState

class AStar(object):
    """
    A* algorithm class, using to solve the puzzle with a given logic.
    A* using the heuristic function inside the logic.
    """

    def __init__(self, logic):
        self._logic = logic

    def search(self, init_state):
        """
        Search the graph from our init state using priority queue of the f-value.
        :param init_state:
        :return: The solution if any.
        """
        import heapq

        priority_queue = []
        init_state.h_cost = self._logic.calc_heuristic(init_state)
        heapq.heappush(priority_queue, (init_state.f_cost, init_state))
        count = 0

        while len(priority_queue):
            current = heapq.heappop(priority_queue)[1]
            count += 1

            if self._logic.is_goal_state(current):
                return backtracking(current), str(count), str(current.g_cost)

            children = [HeuristicState(state=normal_state) for normal_state in self._logic.next_states(current)]

            for son_state in children:
                # update father node
                son_state.came_from = current
                # update the g cost, every move weights 1
                son_state.g_cost = current.g_cost + 1
                # update heuristic value for son
                son_state.h_cost = self._logic.calc_son_heuristic(son_state)
                # push the new son to the priority queue
                heapq.heappush(priority_queue, (son_state.f_cost, son_state))

        # A* is complete, but if there is no answer raise an exception.
        raise Exception('A Star cannot find solution')
