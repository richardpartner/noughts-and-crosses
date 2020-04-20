starting_board =[['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]board = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]taken_turns = 0total_turns = 9def get_value(board, position):    return board[position[0]][position[1]]def get_user_turn(taken_turns):    if taken_turns % 2 == 0:        return 'X'    else:        return '0'def ask_piece(user):    text = 'Where would you like to place your {}?'.format(user)    pos = input(text).strip().lower()    return (int(pos[0]), int(pos[1]))def place_piece(board, position, user):    board[position[0]][position[1]] = user    def is_valid_position(board, position):    if position[0] < 0 or position[0] > 2:        return False    elif position[1] < 0 or position[1] > 2:        return False    elif get_value(board, position) == 'X':        return False    elif get_value(board, position) == '0':        return False    else:        return Truedef check_win(board, user):    if ((board[2][0] == user and board[2][1] == user and board[2][2] == user) or         (board[1][0] == user and board[1][1] == user and board[1][2] == user) or        (board[0][0] == user and board[0][1] == user and board[0][2] == user) or        (board[0][2] == user and board[1][2] == user and board[2][2] == user) or        (board[0][1] == user and board[1][1] == user and board[2][1] == user) or        (board[0][0] == user and board[1][0] == user and board[2][0] == user) or        (board[0][0] == user and board[1][1] == user and board[2][2] == user) or        (board[0][2] == user and board[1][1] == user and board[2][0] == user)):            return 'winner' + userdef check_draw(board):    if board[0][0] != 'A1' and board[0][1] != 'A2' and board[0][2] != 'A3' and board[1][0] != 'B1' and board[1][1] != 'B2' and board[1][2] != 'B3' and board[2][0] != 'C1' and board[2][1] != 'C2' and board[2][2] != 'C3':            return 'draw'def turn(board, user):    pos = ask_piece(user)    if is_valid_position(board, pos):        place_piece(board, pos, user)    else:        print('This is not a valid position!')        turn(board, user)def play_again():    return input('Would you like to play again? (yes or no)').strip().lower()def reset():    if play_again() == 'yes':        taken_turns = 0        board = starting_board    elif play_again() == 'no':        taken_turns = 10        print('Thank you for playing.')print('Welcome to Noughts and Crosses!')        while taken_turns < total_turns:    user_turn = get_user_turn(taken_turns)            if user_turn == 'X':        turn(board, 'X')        if check_win(board, 'X') != 'winnerX':             taken_turns = taken_turns + 1            if check_draw(board) == 'draw':                print('The game is a draw!')                reset()                        else:            print('The winner is X!')            reset()    elif user_turn == '0':        turn(board, '0')        if check_win(board, '0') != 'winner0':             taken_turns = taken_turns + 1            if check_draw(board) == 'draw':                print('The game is a draw!')                reset()        else:            print('The winner is 0!')            reset()                    print(board)