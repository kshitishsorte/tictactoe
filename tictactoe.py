import random

def display_board(position_list):
    
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
    print("\n")


def user_input():
    choice = ""

    while choice != 'X' and choice != 'O':
        choice = input("Please enter X or O: ").upper()

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


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


# check_win(test_board, 'X')

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
    position=-1
    while position not in [0,1,2,3,4,5,6,7,8] or not space_chk(board , position):
        position = int(input("Choose your next position: (0-8) "))

    return position

def replay():
    return input("Do you want to play again (y/n): ").lower().startswith('y')


print("\n\nLets play Tic-Tac-Toe!!!\n\n")

while True:
    board = [" "]*9
    pos_list = []
    for i in range(0, 9):
        pos_list.append(str(i))
    player1_marker, player2_marker = user_input()

    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input("Ready to play? (Yes/No) ")
    if play_game.lower()[0] == 'y':
        gameplay = True
    else:
        gameplay = False

    while gameplay:
        if turn == 'Player 1':
            print("\nChoose the position referring this board")
            display_board(pos_list)
            print("Place your marker")
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if check_win(board, player1_marker):
                display_board(board)
                print("Congratulations, You have WON!!")
                gameplay = False
            else:
                if fullboard_check(board):
                    display_board(board)
                    print("It's a DRAW")
                    break
                else:
                    turn = 'Player 2'
        else:
            print("\nChoose the position referring this board")
            display_board(pos_list)
            print("Place your marker")
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if check_win(board, player2_marker):
                display_board(board)
                print("Congratulations, You have WON!!")
                gameplay = False
            else:
                if fullboard_check(board):
                    display_board(board)
                    print("It's a DRAW")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break



