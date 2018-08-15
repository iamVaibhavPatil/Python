import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_board(board):
    '''
    DESCRIPTION - This function is used to display the current board on screen
    INPUT - Board to be display
    OUTPUT - It will display board on screen
    '''
    clear()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

def select_player_symbol():
    '''
    DESCRIPTION - This method is used to ask Player 1 which kind of keyboard symbol they want
    INPUT - They need to select either X or O
    OUTPUT - Returns tuple with players selection like ('X','O') or ('O','X')
    '''
    marker = ''

    # Get Player-1 to select marker
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Please choose X or O ? ').upper()

    # Based on Player 1 selection, assign marker to Player 2
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, position, marker):
    '''
    DESCRIPTION - This function is used to place marker at position on the board
    '''
    board[position] = marker

def check_if_won(board, mark):    
    '''
    DESCRIPTION - Check if the board to see if win rows have same marker
    '''
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    
    # All column, check to see if marker matches
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or

    # 2 diagonals, check to see match
    (board[1] == mark and board[6] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first():
    '''
    DESCRIPTION - Function used to check, who will play first
    '''
    if random.randrange(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def check_empty_spot(board,position):
    '''
    DESCRIPTION - Check if board has empty spot available at the position
    '''
    return board[position] == ' '

def check_board_full(board):
    '''
    DESCRIPTION - Check if the board is full
    '''
    for i in range(1,10):
        if check_empty_spot(board, i):
            return False

    return True

def player_choice(board):
    '''
    DESCRIPTION - Check if the player choice is between 1-9
    '''
    while True:
        try:
            position = 0
            while position not in [1,2,3,4,5,6,7,8,9] or not check_empty_spot(board, position):
                position = int(input('Choose your next position: (1-9) '))
            break
        except:
            continue

    return position

def replay():
    choice = input('Do you want to play again(y or n)? ').upper()
    return choice == 'Y'


if __name__ == '__main__':
    
    print('Welcome to TIC TAC TOE')

    while True:

        # Set Board
        board = [' ']*10

        # Players and their markers
        player1_marker, player2_marker = select_player_symbol()

        # Choose, who will play first
        turn = choose_first()
        print(turn + ' will go first...')

        # Read to Play
        play_game = input(f'Ready to play {turn} (y or n)? ').upper()

        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        # Play the game
        while game_on:

            if turn == 'Player 1':
                
                # Show the board
                display_board(board)

                # Choose position
                position = player_choice(board)

                # Place marker on position
                place_marker(board, position, player1_marker)

                # Check if won after placing marker
                if check_if_won(board, player1_marker):
                    display_board(board)
                    print('Player 1 has won')
                    game_on = False
                else:
                    # Check if game tie and all position are filled
                    if check_board_full(board):
                        display_board(board)
                        print('Game Tie !!!')
                        game_on = False
                    else:
                        turn = 'Player 2' # No Tie or Win, Player 2 chance

            else:
                # Show the board
                display_board(board)

                # Choose position
                position = player_choice(board)

                # Place marker on position
                place_marker(board, position, player2_marker)

                # Check if won after placing marker
                if check_if_won(board, player2_marker):
                    display_board(board)
                    print('Player 2 has won')
                    game_on = False
                else:
                    # Check if game tie and all position are filled
                    if check_board_full(board):
                        display_board(board)
                        print('Game Tie !!!')
                        game_on = False
                    else:
                        turn = 'Player 1' # No Tie or Win, Player 2 chance                

        # Break from Game, if dont want to replay
        if not replay():
            break
