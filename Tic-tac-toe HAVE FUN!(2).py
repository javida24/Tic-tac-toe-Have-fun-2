# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:51:02 2021

@author: javid
"""


def display_board(board):
    
    print('    THE BOARD  ')
    print(f'  | {board[6]} | {board[7]} | {board[8]} |')  
    print(f'  | {board[3]} | {board[4]} | {board[5]} |')
    print(f'  | {board[0]} | {board[1]} | {board[2]} |')


def player_input():
    
    while True:
        player1 = input("[P1]Please pick a marker 'X' or 'O': ")
        if player1 in ['X', 'O']:
            break
        else:
            print('Please enter correctly!')
    return player1


def place_marker(board, marker, position):
    
    board[position - 1] = marker
    
    return board


def win_check(board, mark):
    
    a = board[0] == board[1] == board[2] == mark
    b = board[3] == board[4] == board[5] == mark
    c = board[6] == board[7] == board[8] == mark
    
    d = board[0] == board[3] == board[6] == mark
    e = board[1] == board[4] == board[7] == mark
    f = board[2] == board[5] == board[8] == mark
    
    g = board[0] == board[4] == board[8] == mark
    h = board[2] == board[4] == board[6] == mark
    
    return a or b or c or d or e or f or g or h


import random

def choose_first():
    return random.randint(1,2)


def space_check(board, position):
    
    return board[position - 1] == ' '


def full_board_check(board):
    
    return ' ' not in board


def player_choice(board):
    
    while True:
        position = input('Please enter position you wanna play:(1-9) ')
        if position in ['1','2','3','4','5','6','7','8','9']:
            position = int(position)
            if space_check(board, position):
                break
            else:
                print('Position is FULL!')
        else:
            print('Please Enter Correctly!')
    
    return position


def replay():
    
    while True:
        replay = input('Do wanna play again? (Y-N)')
        if replay in ['Y', 'N']:
            break
        else:
            print('Sorry i don\'t underestand you!')
    
    return replay == 'Y'


def clear_output():
    print('\n'*100)


print('Welcome to Tic Tac Toe!')

num_board = list(range(1,10))

print('  TEMPLATE BOARD')

display_board(num_board)

while True:
    
    board = [' ']*9
    
    display_board(board)
    
    p1_marker = player_input()
    
    if p1_marker == 'X':
        p2_marker = 'O'
    else:
        p2_marker = 'X'
        
    rank1 = choose_first()
    
    if rank1 == 1:
        print('[P1] should start the game.')
        rank2 = 2
    else:
        print('[P2] should start the game.')
        rank2 = 1
        temp_marker = p1_marker
        p1_marker = p2_marker
        p2_marker = temp_marker
    
    game_on =True
    
    while True:
        
        print(f'[P{rank1} TURN]')

        p1_choice = player_choice(board)

        board = place_marker(board, p1_marker, p1_choice)

        clear_output()
        
        display_board(board)
        
        

        if win_check(board, p1_marker) is True:
            print(f'[P{rank1}] WIN!')
            break

        if full_board_check(board) is True:
            print('DRAW!')
            break

        
        print(f'[P{rank2} TURN]')

        p2_choice = player_choice(board)

        board = place_marker(board, p2_marker, p2_choice)

        clear_output()
        
        display_board(board)

        if win_check(board, p2_marker) is True:
            print(f'[P{rank2}] WIN!')
            break

    if not replay():
        break


# ## Good Job!
