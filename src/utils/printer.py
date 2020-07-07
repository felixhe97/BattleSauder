from .saudertyping import Board, Snake, Coordinates
from typing import List

def printboard(gameboard: Board) -> None:
    for row in gameboard:
        print(row)

def printbattlesnakeboard(gameboard: Board) -> None:
    for j in reversed(range(0, len(gameboard[0]))):
        for i in (range(0, len(gameboard))):
            print(gameboard[i][j], end='', flush=True)
        print('')

def printsnakes(snakes: List[Snake]) -> None:
    for snake in snakes:
        print(snake)

def printfood(food: List[Coordinates]) -> None:
    print(food)