from .utils.constants import EMPTY, SNAKEFOOD, MYSNAKE, OPPONENTS
from .utils.saudertyping import Board, Coordinates, Snake, BattleSnakeResponse
from .logic import nextmove
from typing import Union, List

def parse_snakes(gameboard: Board, snakes: List[Snake]) -> None:
    # mutate snake['id'] to be equivalent to index for easy visual parsing
    snakeindex = MYSNAKE
    for snake in snakes:
        snake['id'] = snakeindex
        for part in snake['body']:
            # each snake part is marked as snakeindex/snake.id
            gameboard[part['x']][part['y']] = snake['id'] 
            snakeindex += 1

def parse_food(matrix: Board, foodarr: List[Coordinates]) -> None:
    for food in foodarr:
        matrix[food['x']][food['y']] = SNAKEFOOD

def init_board(width: int, height: int) -> Board:
    return [[EMPTY] * height for i in range(width)]

def end(jsonobj: dict) -> str:
    return ''

def start(jsonobj: dict) -> str:
    return ''

def move(jsonobj: dict) -> Union[BattleSnakeResponse, str]:
    if 'you' in jsonobj:
        gameboard = initboard(jsonobj['board']['width'], jsonobj['board']['height'])
        food = jsonobj['board']['food']
        parsefood(gameboard, food)
        snakes = jsonobj['board']['snakes']
        parsesnakes(gameboard, snakes)
        playersnake = snakes[0]
        opponentsnakes = snakes[1:]
        return nextmove(gameboard, food, playersnake, opponentsnakes)()
    else:
        return ''