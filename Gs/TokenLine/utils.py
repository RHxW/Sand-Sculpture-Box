def moving_cursor(col_num: int, cur_pos: int, mode: int):
    if mode == 1:  # left
        cur_pos -= 1
    else:  # right
        cur_pos += 1
    return min(max(cur_pos, 0), col_num - 1)

def placing_token(pg:list, cur_pos:int, player_id:int):
    row = 0
    for i in range(len(pg)):
        c = pg[i][cur_pos]
        if c != 0:
            row = i - 1
            break
    pg[row][cur_pos] = player_id
    return pg

def is_win(pg:list, cur_row: int, cur_col:int):
    flg = False
    row_num = len(pg)
    col_num = len(pg[0])
    # row
