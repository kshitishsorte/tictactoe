import random

pos_list = []
for i in range(0, 9):
    pos_list.append(str(i + 1))


def display_board(position_list):
    print("\n"*3)
    print("         |           |          ")
    print(
        f"    {position_list[0]}    |     {position_list[1]}     |     {position_list[2]}")
    print("         |           |          ")
    print("=================================")
    print("         |           |          ")
    print(
        f"    {position_list[3]}    |     {position_list[4]}     |     {position_list[5]}")
    print("         |           |          ")
    print("=================================")
    print("         |           |          ")
    print(
        f"    {position_list[6]}    |     {position_list[7]}     |     {position_list[8]}")
    print("         |           |          ")

test_board = ['X','O','X','O','X','O','X','O','X']
display_board(test_board)

def user_input():
    choice = ""

    while choice != 'X' and choice != 'O':
        choice = input("Please enter X or O: ").upper()

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

user_input()


def place_marker(board, marker, position):
    board[position] = marker


def check_win(board, mark):
    return ((board[0] == board[1] == board[2] == mark) or
    (board[3] == board[4] == board[5] == mark) or
    (board[6] == board[7] == board[8] == mark) or
    (board[0] == board[3] == board[6] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[0] == board[4] == board[8] == mark) or
    (board[2] == board[4] == board[6] == mark))


check_win(test_board, 'X')

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_chk(board, position):
    return board[position] == ' '

def fullboard_check(board):
    for i in range(0,9):
        if space_chk(board, i):
            return False
    return True

def player_choice(board):
    position=0

    while position not in [0,1,2,3,4,5,6,7,8] or not space_chk(board , position):
        position = int(input("Choose your next position: (0-8) "))

    return position

def replay():
    return input("hello")