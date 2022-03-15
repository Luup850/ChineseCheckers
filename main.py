from board import GameBoard
from minimaxAI import AI 
import numpy as np
import copy
import time

#TO DO

#IMPLEMENT THE MINIMAX USING ALL PLAYERS POSSIBLE MOVES. USE GREEDY FOR OTHER PLAYERS(EXISTING ALGORITHM)

#UPDATE THE GOALS TO ONE LOCATION BACKWARDS WHEN A GOAL IS REACHED


game = GameBoard(6)
ai = AI(1)
 

def checkmovement(movefrom,moveto):
    print("MOVEFROM:", movefrom[1:3])

    game.updateBoard(3,[int(movefrom[3:5]), int(movefrom[1:3])], [int(moveto[3:5]), int(moveto[1:3])], 
                        game.playerlist[3].index([int(movefrom[3:5]), int(movefrom[1:3])]))
    
    print(game._board)
    move = ai.chooseMove(game, 1, 1)
    AImoveFrom = 'b{0:02d}{1:02d}'.format(move[1][1], move[1][0])
    AImoveTo = 'b{0:02d}{1:02d}'.format(move[2][1], move[2][0])
    print("To from: {0}, {1}".format(AImoveFrom, AImoveTo))
    #a.updateBoard(1, [10, 2], [12,8], 3)
    print(move[0], move[1], move[2], move[3])
    game.updateBoard(move[0], move[1], move[2], move[3])
    print(game._board)

    return AImoveFrom, AImoveTo

# print(a._board[20,4])
# print(a._board[18,6])

# # player.turn(a)

# print(a._board[20,4])
# print(a._board[18,6])

# print(a._board)

# a._board[0,0] =25  

# print(a._board)

#print(a._board.shape)
# print(a._board)
# move = player.chooseMove(a, 1, 1)
# a.updateBoard(1, [10, 2], [12,8], 3)
# print(move[0], move[1], move[2], move[3])
# a.updateBoard(move[0], move[1], move[2], move[3])
# print(a._board)
#scopy = copy.deepcopy(a._board)
#print(player.findOptimalMove(a, 1))

#print(player.simulateTurn(a, 1)._board)
# %%
