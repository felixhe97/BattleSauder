from queue import SimpleQueue
from typing import Callable
from .utils import FOOD, INDEXSTART, moveup, movedown, moveleft, moveright
from .printer import printbattlesnakeboard, printboard, printfood, printsnakes
import random

def bfsfood(canvisit: list, board: list, myhead: list) -> list:
    q = SimpleQueue()
    q.put(myhead)
    nearestfood = []
    level = 0
    while not q.empty():
        size = q.qsize()
        while size > 0:
            coord = q.get()
            x = coord[0]
            y = coord[1]
            canvisit[x][y] = False
            if board[x][y] == FOOD:
                nearestfood.append((x, y, level))
            if x > 0 and canvisit[x-1][y]:
                q.put((x-1, y))
            if x < len(canvisit) - 1 and canvisit[x+1][y]:
                q.put((x+1, y))
            if y > 0 and canvisit[x][y-1]:
                q.put((x, y-1))
            if y < len(canvisit[0]) - 1 and canvisit[x][y+1]:
                q.put((x, y+1))
            size = size - 1
        level = level + 1
    return nearestfood

def nextmove(board: list, food: list, snakes: list) -> Callable[[], dict]:
    canvisit = [[True] * len(board[0]) for i in range(len(board))]
    for snake in snakes:
        for coord in snake:
            canvisit[coord[0]][coord[1]] = False
    canmove = []
    mysnake = snakes[INDEXSTART]
    myx = mysnake['head'][0]
    myy = mysnake['head'][1]
    if myx > 0 and canvisit[myx-1][myy]:
        canmove.append(moveup)
    if myx < len(board) - 1 and canvisit[myx+1][myy]:
        canmove.append(movedown)
    if myy > 0 and canvisit[myx][myy-1]:
        canmove.append(moveleft)
    if myy < len(board[0]) - 1 and canvisit[myx][myy+1]:
        canmove.append(moveright)
    if mysnake['hp'] < (len(board) * 2) and canmove.count > 0:
        nearestfood = bfsfood(canvisit, board, mysnake['head'])
        nearestfoodx = nearestfood[0]
        nearestfoody = nearestfood[1]
        tofood = []
        if myx < nearestfoodx:
            if movedown in canmove:
                tofood.append(movedown)
        elif myx > nearestfoodx and myx > 0:
            if moveup in canmove:
                tofood.append(moveup)
        if myy < nearestfoody:
            if moveright in canmove:
                tofood.append(moveright)
        elif myy > nearestfoody and myy > 0:
            if moveleft in canmove:
                tofood.append(moveleft)
        if tofood.count > 0:
            return random.choice(tofood)
        elif canmove.count > 0:
            return random.choice(canmove)
        else:
            return moveup
    else:
        if canmove.count == 0:
            return moveup
        else:
            return random.choice(canmove)