from .constants import INDEXSTART

def printboard(board: list) -> None:
    for row in board:
        print(row)

def printbattlesnakeboard(board: list) -> None:
    for j in reversed(range(0, len(board[0]))):
        for i in (range(0, len(board))):
            print(board[i][j], end='', flush=True)
        print('')

def printsnakes(snakes: list) -> None:
    for i in range(INDEXSTART + 1, len(snakes)):
        print(snakes[i])

def printfood(food: list) -> None:
    print(food)