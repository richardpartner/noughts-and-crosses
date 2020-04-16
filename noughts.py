board = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]
taken_turns = 0
total_turns = 9

""" Position is a tuple location (0,1)"""
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

def turn(board, user):
    pos = ask_piece(user)
    if is_valid_position(board, pos):
        place_piece(board, pos, user)
    else:
        print('This is not a valid position!')
        turn(board, user)
        
while taken_turns < total_turns:
    user_turn = get_user_turn(taken_turns)
    
    if user_turn == 'X':
        turn(board, 'X')

    print(board)
