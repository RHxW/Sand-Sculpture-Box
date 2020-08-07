import random
import math
import os


def move_up(board):
    n = len(board)
    cols = [[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                cols[j].append(board[i][j])
    new_cols = [[]for _ in range(n)]
    for i in range(n):
        c = cols[i]
        if len(c) < 2:
            new_cols[i] = c
            continue




def main():
    k = int(input("Board Size(even integer, greater than 2): "))
    while k < 2:
        k = int(input("Board Size(even integer, greater than 2): "))
    board = [[0 for _ in range(k)] for __ in range(k)]
    init_count = min(k, max(2, random.randint(2, k ** 2 // 2) - random.randint(0, k)))
    inits = set()
    while len(inits) != init_count:
        inits.add((random.randint(0,k-1),random.randint(0,k-1)))
    choices = [1]
    for i in range(int(math.log2(k))+1):
        choices.append(2**i)
    for coors in inits:
        board[coors[0]][coors[1]] = random.choice(choices)
    while True:
        for b in board:
            print(b)
        m = input("move(W/S/A/D): ")
        os.system("cls")
        if m in ["w", "W"]:
            pass
        elif m in ["s", "S"]:
            pass
        elif m in ["a", "A"]:
            pass
        elif m in ["d", "D"]:
            pass
        else:
            continue


board = [[0,0,0,0],
         [1,1,1,1],
         [0,2,0,0],
         [1,2,0,1]
         ]
move_up(board)