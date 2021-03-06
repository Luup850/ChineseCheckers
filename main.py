from genericpath import isfile
from board import GameBoard
from MaxN import AI 
import numpy as np
import copy
import time



game = GameBoard(6)
ai1 = AI(1)
ai2 = AI(2)
ai3 = AI(3)
ai5 = AI(5)
ai6 = AI(6)
 
player_list = game.playerlist.copy()
def checkmovement(movefrom,moveto):
    print("MOVEFROM:", movefrom[1:3])
    list_of_ais = [ai1, ai2, ai3, ai5, ai6]
    AImoveFrom = []
    AImoveTo = []
    order_of_ais = []
    game.updateBoard(3,[int(movefrom[3:5]), int(movefrom[1:3])], [int(moveto[3:5]), int(moveto[1:3])], 
                        game.playerlist[3].index([int(movefrom[3:5]), int(movefrom[1:3])]))
    
    print(game._board)
    for ai in list_of_ais:
        move = ai.chooseMove(game, 1, 1)
        order_of_ais.append(ai.player_no)
        AImoveFrom.append('b{0:02d}{1:02d}'.format(move[1][1], move[1][0]))
        AImoveTo.append('b{0:02d}{1:02d}'.format(move[2][1], move[2][0]))
        #print("To from: {0}, {1}".format(AImoveFrom, AImoveTo))
        #a.updateBoard(1, [10, 2], [12,8], 3)
        #print(move[0], move[1], move[2], move[3])
        game.updateBoard(move[0], move[1], move[2], move[3])
        #print(game._board)

    for i in list_of_ais:
        if (i.isFinished(game, i.player_no)):
            print("AI PLAYER" +str(i.player_no + "WINS"))
            game.updateGoalList(i.player_no, player_list)
    if(i.isFinished(game, 3)):
        print("YOU WIN")
    

    return order_of_ais ,AImoveFrom, AImoveTo

