col_num = 7
row_num = 7

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

player_token = {
    0: "⓪",
    1: "①",
    2: "②",
    3: "③",
    4: "④",
    5: "⑤",
    6: "⑥",
    7: "⑦",
    8: "⑧",
    9: "⑨",
    999: "۞",
    1000: "۝",
    9999: "۩",
    10000: "֎"

}


pg = [[0 for c in range(col_num)] for r in range(row_num)]
for i in range(row_num):
    if i == 0:
        print(table_chrs[3] + table_chrs[1] * (int(col_num * 3) + col_num-1) + table_chrs[4])
    s = table_chrs[2]
    for p in pg[i]:
        if p == 0:
            # s += " _ "
            s += " " + " " + " " + table_chrs[2]
            # s += " " + '\033[1;32;0m%s\033[0m' % str(p) + " " + table_chrs[2]
        else:
            s += " " + '\033[1;32;0m%s\033[0m' % str(p) + " " + table_chrs[2]
    # if s[-1] != table_chrs[2]:
    #     s += table_chrs[2]
    print(s)
    if i == row_num - 1:
        break
    print(table_chrs[7] + table_chrs[1] * (int(col_num * 3) + col_num-1) + table_chrs[8])
print(table_chrs[5] + table_chrs[1] * (int(col_num * 3) + col_num-1) + table_chrs[6])
