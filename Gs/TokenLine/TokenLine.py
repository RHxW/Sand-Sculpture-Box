import os
import os

import msvcrt
from GetPlayGround import *
from utils import *


def main(row_num: int = 7, col_num: int = 7, player_num: int = 2, win_cond: int = 4):
    while win_cond < 4 or win_cond > 10:
        print("Win Condition should be 4 to 10.")
        win_cond = input("Win Condition: ")
    while row_num < 5 or col_num < 5 or row_num > 15 or col_num or row_num * col_num < win_cond ** 2:
        print("The number of row or column is not valid.")
        row_num = input("Number of row: ")
        col_num = input("Number of column: ")
    pg = [[" " for c in range(col_num)] for r in range(row_num)]
    cur_pos = 0
    players = [_ for _ in range(1, player_num + 1)]
    while True:
        for player in players:
            get_play_ground_display()
            while True:
                ch = msvcrt.getch()
                if ch[0] == 27:  # esc
                    os.system('cls')
                    exit(0)
                # elif ch[0] == 119:  # w
                #     pass
                # elif ch[0] == 115:  # s
                #     pass
                elif ch[0] == 97:  # a-left
                    cur_pos = moving_cursor(col_num, cur_pos, 1)
                    if pg[0][cur_pos] != 0:
                        continue
                    pg = placing_token(pg, cur_pos, player)

                elif ch[0] == 100:  # d-right
                    cur_pos = moving_cursor(col_num, cur_pos, 2)
                elif ch[0] in [32, 13]:  # space/enter
                    pass

    # oldstdout = sys.stdout
    # for p in pg:
    #     print(p)
    # time.sleep(1)
    # os.system('cls')
    # sys.stdout = oldstdout
    # for p in pg:
    #     print(p)
    # os.system('cls')


main()
