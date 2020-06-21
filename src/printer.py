def printboard(board: list) -> None:
    for row in board:
        print(row)

def printbattlesnakeboard(board: list) -> None:
    for i in reversed(range(0, len(board[0]))):
        for j in reversed(range(0, len(board))):
            print(board[j][i], end='', flush=True)
        print('')

def printsnakes(snakes: dict) -> None:
    for i, snake in snakes.items():
        print(i, snake)

def printfood(food: list) -> None:
    for x in food:
        print(x)