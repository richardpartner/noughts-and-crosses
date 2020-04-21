def set_game():
    global board
    global taken_turns
    global total_turns
    global outcome

    board = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]
    taken_turns = 0
    total_turns = 9
    outcome = None

def get_value(board, position):
    return board[position[0]][position[1]]

def get_user_turn(taken_turns):
    if taken_turns % 2 == 0:
        return 'X'
    else:
        return '0'

def ask_piece(user):
    text = 'Where would you like to place your {}?'.format(user)
    pos = input(text).strip().lower()
    return (int(pos[0]), int(pos[1]))

def place_piece(board, position, user):
    board[position[0]][position[1]] = user
    
def is_valid_position(board, position):
    if position[0] < 0 or position[0] > 2:
        return False
    elif position[1] < 0 or position[1] > 2:
        return False
    elif get_value(board, position) == 'X':
        return False
    elif get_value(board, position) == '0':
        return False
    else:
        return True

def check_win(matrix):
    for row in matrix:
        if row[0] == row[1] == row[2]:
            return True
    return False

def get_row_matrix(board):
    return board

def get_col_matrix(board):
    cols = []
    for i in range(len(board)):
        cols.append([row[i] for row in board])
    return cols

def get_diag_matrix(board):
    left_diag = [board[i][len(board)-1-i] for i in range(len(board))]
    right_diag = [board[i][i] for i in range(len(board))]
    return [left_diag, right_diag]


def is_user_piece(board, position):
    if get_value(board, position) in ['X','O']:
        return True
    else:
        return False

def check_draw(matrix):
    draw = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not is_user_piece(matrix, (i,j)):
                draw = False
    return draw

def check_outcome(board, user):

    global outcome
    
    if check_win(get_row_matrix(board)):
        outcome = user + ' wins'
    elif check_win(get_col_matrix(board)):
        outcome = user + ' wins'
    elif check_win(get_diag_matrix(board)):
        outcome = user + ' wins'
    elif check_draw(board):
        outcome = 'The game is a draw'
    print(outcome)

def turn(board, user):
    pos = ask_piece(user)
    if is_valid_position(board, pos):
        place_piece(board, pos, user)
        check_outcome(board, user)
        global taken_turns
        taken_turns = taken_turns + 1
    else:
        print('This is not a valid position!')
        turn(board, user)

def play_again():
    return input('Would you like to play again? (yes or no)').strip().lower()

def reset():
    if play_again() == 'yes':
        play_game()
    else:
        print('Thank you for playing.')

def play_game():

    print('Welcome to Noughts and Crosses!')

    set_game()
    
    global outcome
    while taken_turns < total_turns and outcome == None:
        user_turn = get_user_turn(taken_turns)
            
        if user_turn == 'X':
            turn(board, 'X')
            
        elif user_turn == '0':
            turn(board, '0')
                    
        print(board)

    if outcome != None:
        reset()
