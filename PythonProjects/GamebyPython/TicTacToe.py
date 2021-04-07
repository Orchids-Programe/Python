from random import randint
board = [0,1,2,3,4,5,6,7,8]
def print_board(x1,x2,x3):
    print('|', board[x1], '|', board[x2], '|',board[x3], '|')
    print('-------------')

def show():
    print_board(0,1,2)
    print_board(3,4,5)
    print_board(6,7,8)
show()

def empty_box():
    for x in range(0,9):
        if board[x] != 'x' and board[x] != 'o':
            return True

def check_line(check, x1, x2, x3):
    if board[x1] == check and board[x2] == check and board[x3] == check:
        return True
    return False

def check_all(check):
    if check_line(check,0,1,2):
        return True
    if check_line(check,3,4,5):
        return True
    if check_line(check,6,7,8):
        return True
    if check_line(check,0,4,8):
        return True
    if check_line(check,6,4,2):
        return True
    if check_line(check,0,3,6):
        return True
    if check_line(check,1,4,7):
        return True
    if check_line(check,2,5,8):
        return True
    return False

#ket qua hoa = 0
win = 0
while empty_box():
    cell = int(input('Please enter a cell No. (0-8): '))
    if board[cell] == 'x' or board[cell] == 'o':
        print('Blank space has been filled')
    else:
        board[cell] = 'x'
        while empty_box():
            computer = randint(0,8)
            if board[computer] == 'x' or board[computer] == 'o':
                pass
            else:
                board[computer] = 'o'
                break
    show()
    if check_all('x'):
        win = '___YOU WIN___'
        break
    if check_all('o'):
        win = '___YOU LOST___'
        break
if win == 0:
    print('Draw')
else:
    print(win)
