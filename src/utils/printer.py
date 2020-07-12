from .saudertyping import Board, Snake, Coordinates
from typing import List

def print_game_board(gameboard: Board) -> None:
    for row in gameboard:
        print(row)

def print_battlesnake_board(gameboard: Board) -> None:
    for j in reversed(range(0, len(gameboard[0]))):
        for i in (range(0, len(gameboard))):
            print(gameboard[i][j], end='', flush=True)
        print('')

def print_snakes(snakes: List[Snake]) -> None:
    for snake in snakes:
        print(snake)

def print_food(food: List[Coordinates]) -> None:
    print(food)