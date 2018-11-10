from TilePuzzleLogic import backtracking
from PuzzleState import HeuristicState

class AStar(object):

    def __init__(self, logic):
        self._logic = logic

    def search(self, init_state):
        import heapq

        priority_queue = []
        closed_list = set()
        init_state.h_cost = self._logic.calc_heuristic(init_state)
        heapq.heappush(priority_queue, (init_state.f_cost, init_state))

        while len(priority_queue):
            current = heapq.heappop(priority_queue)[1]
            closed_list.add(current)

            if self._logic.is_goal_state(current):
                return backtracking(current), str(len(closed_list)), str(current.g_cost)

            children = [HeuristicState(state=normal_state) for normal_state in self._logic.next_states(current)]

            for son_state in children:
                if son_state not in closed_list:
                    # update father node
                    son_state.came_from = current
                    # update the g cost, every move weights 1
                    son_state.g_cost = current.g_cost + 1
                    # update heuristic value for son
                    son_state.h_cost = self._logic.calc_heuristic(son_state)

                    heapq.heappush(priority_queue, (son_state.f_cost, son_state))

        raise Exception('A Star cannot find solution')
