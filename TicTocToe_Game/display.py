
""" HERE IS THE MOST INTERESTING GAME FOR YOU " TIC TAC TOE " !!  
    THIS GAME REQUIRES TWO PLAYERS. BOTH CAN SELECT THEIR MARKER ['X','O']
    AS PER THEIR WISH.
    ONE PLAYER WILL SELECT THEIR POSITION TO INSERT THEIR MARKER AND THEN SECOND PLAYER.
    IF ANY PLAYER'S WINS THEN IT WILL DISPLAY ACCORDING TO THAT.
    I HOPE YOU GUYS WILL LOVE IT. 
    !!!!!!!!   THANK YOU !!!!!!!!!!
"""
""" @Author :- Md Asif
    @Email : - imd.asif222@gmail.com
"""
def display_board(board):
    print("\n**************************************")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

test_board=['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#display_board(test_board)

def player_input():
    marker = ""
    while marker !='X' and marker !='O':
        marker = input("\nPlayer 1 : Choose X or O \n").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#player1_marker,player2_marker = player_input()
#print(player1_marker)

def place_marker(board,marker,position):
    board[position] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9]== mark)  or
    (board[4] == mark and board[5] == mark and board[6]== mark) or
    (board[1] == mark and board[2] == mark and board[3]== mark) or
    (board[7] == mark and board[4] == mark and board[1]== mark) or
    (board[8] == mark and board[5] == mark and board[2]== mark) or
    (board[9] == mark and board[6] == mark and board[3]== mark) or
    (board[7] == mark and board[5] == mark and board[3]== mark) or
    (board[9] == mark and board[5] == mark and board[1]==mark))

# display_board(test_board)
# print(win_check(test_board,'X'))

import dis
import random
from turtle import position
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] == ' ' 

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("\n!!! Choose a position (1-9) !!!\n"))
    return position

def replay():
    choice = input("\n!!! Wanna play again? Enter Yes or No !!!\n")
    return choice == 'Yes'


print("\n\n!!  Welcome to Tic Tac Toe Game !! ")
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn =choose_first()
    print("\n"+ turn + ' Will go first')
    
    play_game = input("\n !!! Ready to play? y or n? !!!\n ")
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("\n!!! Yaahoo Player 1 Has Won !! Well Played !!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\n!!! Tie Game Well Played !!!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("\n!!! Yaahoo Player 2 Has Won !! Well Played !!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\n!!!  Tie Game Well Played !!!!")
                    game_on = False
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
            
                    
