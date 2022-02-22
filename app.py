def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
display_board(test_board)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

player1_marker, player2_marker = player_input()

# Place marker
def place_marker(board, marker, position):
    board[position] = marker

# Test function place_marker
place_marker(test_board, '$', 8)
display_board(test_board)

# Check winner
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

win_check(test_board, 'X')

# Choose player
import random
from turtle import pos
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else: 
        return 'Player 2'

# Check space in board position
def space_check(board, position):
    return board[position] == ' '

# Check if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False 
    #Board is full
    return True

# Choose position on board
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))

    return position

# Check if player want to play again
def replay():
    choice = input('Play again? Enter yes or no')
    return choice == 'Yes'

# The game logic itself
print('Welcome to Tic Tac Toe!')
while True:

    ## Setup
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? type y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Gameplay
    while game_on:
        # Player 1 turn
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)

            # Choose the position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False

        else:
            # Check if there is a tie
            if full_board_check(the_board):
                display_board()
                print("Tie game..")
                game_on = False
            else:
                turn = 'Player 2'

    if not replay():
        break