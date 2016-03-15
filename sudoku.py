def solve(sudoku):
    return sudoku

def check_row(sudoku, x, y, val):
    for ix in range(9):
        if x == ix: continue
        if sudoku[ix][y] == val: return False
    return True

def check_column(sudoku, x, y, val):
    for iy in range(9):
        if y == iy: continue
        if sudoku[x][iy] == val: return False
    return True

def check_cell(sudoku, x, y, val):
    sx = x - (x % 3)
    sy = y - (y % 3)
    for ix in range(sx, sx + 3):
        for iy in range(sy, sy + 3):
            if y == iy and x == ix: continue
            if sudoku[ix][iy] == val: return False
    return True
