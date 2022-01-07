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
    if ((board[0] == board[1] == board[2] == mark) or
    (board[3] == board[4] == board[5] == mark) or
    (board[6] == board[7] == board[8] == mark) or
    (board[0] == board[3] == board[6] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[0] == board[4] == board[8] == mark) or
    (board[2] == board[4] == board[6] == mark)):
        print("True")
    else:
        print("False")


check_win(test_board, 'X')

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_chk(board, position):
    
    # while position_list[0] != position_list[1] != position_list[2] != 'X' or position_list[3] != position_list[4] != \
    #         position_list[5] != 'X' or position_list[6] != position_list[7] != position_list[8] != 'X' or position_list[
    #     0] != position_list[3] != position_list[6] != 'X' or position_list[1] != position_list[4] != position_list[
    #     7] != 'X' or position_list[2] != position_list[5] != position_list[8] != 'X' or position_list[0] != \
    #         position_list[4] != position_list[8] != 'X' or position_list[2] != position_list[4] != position_list[
    #     6] != 'X' or position_list[0] != position_list[1] != position_list[2] != 'O' or position_list[3] != \
    #         position_list[4] != position_list[5] != 'O' or position_list[6] != position_list[7] != position_list[
    #     8] != 'O' or position_list[0] != position_list[3] != position_list[6] != 'O' or position_list[1] != \
    #         position_list[4] != position_list[7] != 'O' or position_list[2] != position_list[5] != position_list[
    #     8] != 'O' or position_list[0] != position_list[4] != position_list[8] != 'O' or position_list[2] != \
    #         position_list[4] != position_list[6] != 'O':
    #     pos = int(input("Enter the position "))
    #     marker = choice

    #     if pos == 1:
    #         position_list[0] = marker
    #     if pos == 2:
    #         position_list[1] = marker
    #     if pos == 3:
    #         position_list[2] = marker
    #     if pos == 4:
    #         position_list[3] = marker
    #     if pos == 5:
    #         position_list[4] = marker
    #     if pos == 6:
    #         position_list[5] = marker
    #     if pos == 7:
    #         position_list[6] = marker
    #     if pos == 8:
    #         position_list[7] = marker
    #     if pos == 9:
    #         position_list[8] = marker
    #     display_board(pos_list)

    # pos = int(input("Enter the position "))
    # marker = choice
    #
    # if pos == 1:
    #     position_list[0] = marker
    # if pos == 2:
    #     position_list[1] = marker
    # if pos == 3:
    #     position_list[2] = marker
    # if pos == 4:
    #     position_list[3] = marker
    # if pos == 5:
    #     position_list[4] = marker
    # if pos == 6:
    #     position_list[5] = marker
    # if pos == 7:
    #     position_list[6] = marker
    # if pos == 8:
    #     position_list[7] = marker
    # if pos == 9:
    #     position_list[8] = marker
    # display_board(pos_list)


#game_play(pos_list, choice)





