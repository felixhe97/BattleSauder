from .constants import INDEXSTART
from typing import List
from .saudertyping import Board

def printboard(board: Board) -> None:
    for row in board:
        print(row)

def printbattlesnakeboard(board: Board) -> None:
    for j in reversed(range(0, len(board[0]))):
        for i in (range(0, len(board))):
            print(board[i][j], end='', flush=True)
        print('')

def printsnakes(snakes: List) -> None:
    for i in range(INDEXSTART + 1, len(snakes)):
        print(snakes[i])

def printfood(food: List) -> None:
    print(food)