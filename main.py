#%%
from board import GameBoard
#from minimaxAI import AI 
from minimaxAI_v2 import MinimaxAI_v2 as AI_v2
import numpy as np
import copy
import time

#TO DO

#IMPLEMENT THE MINIMAX USING ALL PLAYERS POSSIBLE MOVES. USE GREEDY FOR OTHER PLAYERS(EXISTING ALGORITHM)

#UPDATE THE GOALS TO ONE LOCATION BACKWARDS WHEN A GOAL IS REACHED
game = GameBoard(6)
#ai1 = AI_v2(1, [4])
ai4 = AI_v2(4, [1])

flipflop = True
tick = 0
move = []
move2 = []
print("First board:", game._board)
while(game.check_win_condition() == 0 and 1 != 50):
    time.sleep(1)
    game.board_name = 'Main'
    #print("Turn:", tick)
    if(flipflop):
        game_copy = copy.deepcopy(game)
        ai1 = AI_v2(1, [4])
        move1 = ai1.take_turn(game_copy)
        print("Player 1 took turn:", move1)
        #print("[DEBUG]: {0} {1}".format(game._board[move1[0][0], move1[0][1]], game._board[move1[1][0], move1[1][1]]))
        game.update_board(move1[0], move1[1])
        #print("[DEBUG]: {0} {1}".format(game._board[move1[0][0], move1[0][1]], game._board[move1[1][0], move1[1][1]]))
        #print(game.board_name)
        #flipflop = False
    else:
        game_copy = copy.deepcopy(game)
        move4 = ai4.take_turn(game_copy)
        print("Player 4 took turn:", move4)
        #print("[DEBUG]: {0} {1}".format(game._board[move4[0][0], move4[0][1]], game._board[move4[1][0], move4[1][1]]))
        game.update_board(move4[0], move4[1])
        #print("[DEBUG]: {0} {1}".format(game._board[move4[0][0], move4[0][1]], game._board[move4[1][0], move4[1][1]]))
        #print(game.board_name)
        flipflop = True
    
    if(tick > 20):
        tick = 0
        print(game._board)
    else:
        tick = tick + 1

#var = copy.deepcopy(game._board)
print(game._board)

# game = GameBoard(6)
# ai1 = AI(1)
# ai2 = AI(2)
# ai3 = AI(3)
# ai5 = AI(5)
# ai6 = AI(6)
 

# def checkmovement(movefrom,moveto):
#     print("MOVEFROM:", movefrom[1:3])
#     list_of_ais = [ai1, ai2, ai3, ai5, ai6]
#     AImoveFrom = []
#     AImoveTo = []
#     order_of_ais = []
#     game.updateBoard(3,[int(movefrom[3:5]), int(movefrom[1:3])], [int(moveto[3:5]), int(moveto[1:3])], 
#                         game.playerlist[3].index([int(movefrom[3:5]), int(movefrom[1:3])]))
    
#     print(game._board)
#     for ai in list_of_ais:
#         move = ai.chooseMove(game, 1, 1)
#         order_of_ais.append(ai.player_no)
#         AImoveFrom.append('b{0:02d}{1:02d}'.format(move[1][1], move[1][0]))
#         AImoveTo.append('b{0:02d}{1:02d}'.format(move[2][1], move[2][0]))
#         #print("To from: {0}, {1}".format(AImoveFrom, AImoveTo))
#         #a.updateBoard(1, [10, 2], [12,8], 3)
#         #print(move[0], move[1], move[2], move[3])
#         game.updateBoard(move[0], move[1], move[2], move[3])
#         #print(game._board)

#     return order_of_ais ,AImoveFrom, AImoveTo
# %%
