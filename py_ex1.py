from PuzzleState import State, HeuristicState
from TilePuzzleLogic import TilePuzzleLogic
from BFS import BFS_Seaerch
from IDFS import IDFS
from AStar import AStar
from Board import Board

def write_results(result):
    """
    Write the results of the given puzzle.
    :param result: The results of the puzzle.
    :return: None.
    """
    output_file = open('output.txt', 'w')
    output_file.write(' '.join(result))
    output_file.close()

def solve_tile_puzzle(selected_algo, n, given_array):
    """
    Using the selected algorithm solve the given array by n x n matrix. Write the output in a different file.
    :param selected_algo: 1 - IDS, 2 - BFS, 3 - A*
    :param n: Number of dimension in the puzzle.
    :param given_array: The array of the puzzle.
    :return: None.
    """
    logic = TilePuzzleLogic(n)
    board = Board(array=given_array)
    board.find_space()

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
    return result

def make_board_from_string(string, n):
    """
    Return a 2D array (n x n) representing the string.
    :param string: The numbers in the puzzle separated by '-'.
    :param n: The dimension of the puzzle.
    :return: The 2D array.
    """

    split_board = string.split('-')
    ans = []

    for row in range(n):
        row_to_add = []
        for col in range(n):
            row_to_add.append(int(split_board[row * n + col]))
        ans.append(row_to_add)
    return ans


def main():
    """
    Opening the input file and writing the solving results into output.
    :return: None.
    """
    input_file = open('AI-EX1-TestS/input_elad3.txt', 'r')
    args = input_file.read().splitlines()
    input_file.close()
    selected_algorithm = int(args[0])
    n = int(args[1])
    board = make_board_from_string(args[2], n)

    result = solve_tile_puzzle(selected_algorithm, n, board)
    write_results(result)

if __name__ == '__main__':
    main()
