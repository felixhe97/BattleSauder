from queue import SimpleQueue
from typing import Callable
from .utils import FOOD, INDEXSTART, moveup, movedown, moveleft, moveright
import random

"""
def distance(x: int, y: int):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
"""

def bfsfood(canvisit: list[list[bool]], board: list[list[int]], myhead: list[int]) -> list[list[int]]:
    q = SimpleQueue()
    q.put(myhead)
    nearestfood = []
    level = 0
    while not q.empty():
        qsize = q.qsize()
        while qsize > 0:
            coord = q.get()
            x = coord[0]    
            y = coord[1]
            canvisit[x][y] = False
            if board[x][y] == FOOD:
                nearestfood.append([x, y, level])
            if x > 0 and canvisit[x-1][y]:
                q.put([x-1, y])
            if x < len(canvisit) - 1 and canvisit[x+1][y]:
                q.put([x+1, y])
            if coord[1] > 0 and canvisit[x][y-1]:
                q.put([x, y-1])
            if coord[1] < len(canvisit[0]) - 1 and canvisit[x][y+1]:
                q.put([x, y+1])
            qsize = qsize - 1
        level = level + 1
    return nearestfood

def nextmove(board: list[list[int]], food: list[list], snakes: list[dict]) -> Callable[[], dict]:
    q = SimpleQueue()
    canvisit = [[True] * len(board) for i in range(len(board[0]))]
    mysnake = snakes[INDEXSTART]
    nearbyopenspace = []
    myx = mysnake['head'][0]
    myy = mysnake['head'][1]
    if myx > 0 and canvisit[myx-1][myy]:
        nearbyopenspace.append(moveup)
    if myx < len(board) and canvisit[myx+1][myy]:
        nearbyopenspace.append(movedown)
    if myy > 0 and canvisit[myx][myy-1]:
        nearbyopenspace.append(moveleft)
    if myy < len(board[0]) and canvisit[myx][myy+1]:
        nearbyopenspace.append(moveright)
    for snake in snakes:
        for coord in snake['body']:
            canvisit[coord[0]][coord[1]] = False
        if snake != mysnake and snake['hp'] > mysnake['hp']:
            enemyx = snake['head'][0]
            enemyy = snake['head'][1]
            if enemyx > 0:
                canvisit[enemyx-1][enemyy] = False
            if enemyx < len(board) - 1:
                canvisit[enemyx+1][enemyy] = False
            if enemyy > 0:
                canvisit[enemyx][enemyy-1] = False
            if enemyy < len(board[0]) - 1:
                canvisit[enemyx][enemyy+1] = False  
    canmove = []
    if myx > 0 and canvisit[myx-1][myy]:
        canmove.append(moveup)
    if myx < len(board) and canvisit[myx+1][myy]:
        canmove.append(movedown)
    if myy > 0 and canvisit[myx][myy-1]:
        canmove.append(moveleft)
    if myy < len(board[0]) and canvisit[myx][myy+1]:
        canmove.append(moveright)
    if mysnake['hp'] < (len(board) * 2) and canmove.count > 0:
        nearestfood = bfsfood(canvisit, board, mysnake['head'])
        tofood = []
        if myx < nearestfood[0][0]:
            if movedown in canmove:
                tofood.append(movedown)
        elif myx > nearestfood[0][0] and nearestfood[0][0] != 0:
            if moveup in canmove:
                tofood.append(moveup)
        if myy < nearestfood[0][1]:
            if moveright in canmove:
                tofood.append(moveright)
        elif myy > nearestfood[0][1] and nearestfood[0][1] != 0:
            if moveleft in canmove:
                tofood.append(moveleft)
        return random.choice(tofood)
    else:
        if canmove.count == 0:
            if nearbyopenspace.count == 0:
                return moveup()
            else:
                return random.choice(nearbyopenspace)
        else:
            return random.choice(canmove)
