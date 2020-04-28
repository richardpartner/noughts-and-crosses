import pytest
import copy
from noughts import *

board1 = [['X','0','X'],['0','0','X'],['0','X','X']]
board2 = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]
board3 = [['X','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]

turns_taken = 3

def test_get_value():
    assert get_value(board1, (0,0)) == 'X'
    assert get_value(board1, (1,1)) == '0'
    
def test_place_piece():
    board2_copy = copy.deepcopy(board2)
    place_piece(board2_copy, (0,0), 'X')
    assert board2_copy == board3

def test_is_user_piece():
    assert is_user_piece(board1, (0,1)) == True

def test_get_user_turn():
    assert get_user_turn(turns_taken) == '0'

def test_is_valid_position():
    assert is_valid_position(board3,(0,0)) == False
    assert is_valid_position(board3,(0,1)) == True

