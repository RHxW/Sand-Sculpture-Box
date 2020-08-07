import os

table_chrs = {
    1: "─",
    2: "│",
    3: "┌",
    4: "┐",
    5: "└",
    6: "┘",
    7: "├",
    8: "┤",
    9: "┬",
    10: "┴",
    11: "┼"
}


def get_play_ground_display(pg: list, row_num:int, col_num:int, cur_player: int, cur_pos: int, is_over: bool = False, over_at: list = []):
    os.system("cls")
    print("Current Player ID: %d" % cur_player)
    for i in range(row_num):
        if i == 0:
            print(table_chrs[3] + table_chrs[1] * (int(col_num * 3) + col_num - 1) + table_chrs[4])
        s = table_chrs[2]
        for p in pg[i]:
            if p == 0:
                # s += "   "
                s += "   " + table_chrs[2]
                # s += " " + '\033[1;32;0m%s\033[0m' % str(p) + " " + table_chrs[2]
            else:
                s += " " + '\033[1;32;0m%s\033[0m' % str(p) + " " + table_chrs[2]
        print(s)
        if i == row_num - 1:
            break
        print(table_chrs[7] + table_chrs[1] * (int(col_num * 3) + col_num - 1) + table_chrs[8])
    print(table_chrs[5] + table_chrs[1] * (int(col_num * 3) + col_num - 1) + table_chrs[6])
