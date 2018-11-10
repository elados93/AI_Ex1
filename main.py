from PuzzleState import State, HeuristicState
from TilePuzzleLogic import TilePuzzleLogic
from BFS import BFS_Seaerch
from IDFS import IDFS
from AStar import AStar

def write_results(result):
    # route, developed_nodes, solution_depth = result[0], result[1], result[2]
    
    with open('output.txt', 'w') as output_file:
        output_file.write(' '.join(result))

def solve_tile_puzzle(selected_algo, n, board):

    logic = TilePuzzleLogic(n)

    result = None
    if selected_algo == 1:
        idfs = IDFS(logic)
        result = idfs.search(State(board))        
    elif selected_algo == 2:
        bfs = BFS_Seaerch(logic)
        result = bfs.search(State(board))
    elif selected_algo == 3:
        a_star = AStar(logic)
        result = a_star.search(HeuristicState(board))
    else:
        raise Exception('Bad input! no such search algorithm')
    write_results(result)

def make_board_from_string(string, n):
    split_board = string.split('-')
    ans = []

    for row in range(n):
        row_to_add = []
        for col in range(n):
            row_to_add.append(split_board[row * n + col])
        ans.append(row_to_add)
    return  ans

def main():
    with open('input.txt') as input_file:
        args = input_file.read().splitlines()
    selected_algorithm = int(args[0])
    n = int(args[1])
    board = make_board_from_string(args[2], n)

    solve_tile_puzzle(selected_algorithm, n, board)

if __name__ == '__main__':
    main()
