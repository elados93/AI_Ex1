from TilePuzzleLogic import backtracking

class BFS_Seaerch(object):

    def __init__(self, logic):
        self._logic = logic

    def search(self, init_state):
        open_list = []
        closed_list = set()

        open_list.append(init_state)

        while len(open_list):
            current = open_list.pop(0)
            closed_list.add(current)

            if self._logic.is_goal_state(current):
                return backtracking(current), str(len(closed_list)), '0'

            children = self._logic.next_states(current)

            for child in children:
                if child not in closed_list:
                    open_list.append(child)

        raise Exception('Puzzle is not solvable!')
