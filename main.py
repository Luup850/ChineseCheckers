from board import GameBoard
from minimaxAI import AI 
import numpy as np
import copy
#TO DO

#IMPLEMENT THE MINIMAX USING ALL PLAYERS POSSIBLE MOVES. USE GREEDY FOR OTHER PLAYERS(EXISTING ALGORITHM)

#UPDATE THE GOALS TO ONE LOCATION BACKWARDS WHEN A GOAL IS REACHED


a = GameBoard(6)
player = AI(1)
 


# print(a._board[20,4])
# print(a._board[18,6])

# # player.turn(a)

# print(a._board[20,4])
# print(a._board[18,6])

# print(a._board)

# a._board[0,0] =25  

# print(a._board)

#print(a._board.shape)
#print(a._board)
player.chooseMove(a, 1)
# copy = copy.deepcopy(a._board)
#print(player.findOptimalMove(a, 1))

#print(player.simulateTurn(a, 1)._board)