def printboard(board: list) -> None:
    for row in board:
        print(row)

def printsnakes(snakes: dict) -> None:
    for i, snake in snakes.items():
        print(i, snake)

def printfood(food: list) -> None:
    for x in food:
        print(x)