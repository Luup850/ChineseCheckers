from re import X
import numpy as np
import math
import sys
import random

sys.setrecursionlimit(9999)

class GameBoard:
    _board = np.zeros((25, 17))
    _goalpos = []
    number_of_players = 0
    # Taken from https://github.com/AndreaVidali/ChineseChekersAI/blob/master/engine_2.py which is why x and y is flipped
    player1 = [[12, 0], [11, 1], [13, 1], [10, 2], [12, 2], [14, 2], [9, 3], [11, 3], [13, 3], [15, 3]]
    player2 = [[18, 4], [20, 4], [22, 4], [24, 4], [19, 5], [21, 5], [23, 5], [20, 6], [22, 6], [21, 7]]
    player3 = [[21, 9], [20, 10], [22, 10], [19, 11], [21, 11], [23, 11], [18, 12], [20, 12], [22, 12], [24, 12]]
    player4 = [[9, 13], [11, 13], [13, 13], [15, 13], [10, 14], [12, 14], [14, 14], [11, 15], [13, 15], [12, 16]]
    player5 = [[3, 9], [2, 10], [4, 10], [1, 11], [3, 11], [5, 11], [0, 12], [2, 12], [4, 12], [6, 12]]
    player6 = [[0, 4], [2, 4], [4, 4], [6, 4], [1, 5], [3, 5], [5, 5], [2, 6], [4, 6], [3, 7]]
    
    
    playerlist = [player1, player2, player3, player4, player5, player6]
    goalList = [[12, 16], [0, 12], [0, 4] ,[12, 0], [24, 4], [24, 12]]
    #Takes a tuple of 6, indicating players
    def __init__(self, players):
        #Invalid positions to move to
        self.number_of_players = players
        border =    [[10,0], [9,1], [8,2], [7,3], [5,3], [3,3], [1,3],
                     [0,6], [1,7], [2,8], [2,9], [0,10],
                     [1,13], [3,13], [5,13], [7,13], [8,14], [9,15], [10,16],
                     [14,16], [15,15], [16,14], [17,13], [19,13], [21,13], [23,13],
                     [24,10], [23,9], [22,8], [23,7], [24,6],
                     [23,3], [21,3], [19,3], [17,3], [16,2], [15,1], [14,0]]
        #Place border on board
        for x, y in border:
            self._board[x,y] = -1

        #Put players on the board
        for i in range(1, 6 + 1):
            for x,y in self.playerlist[i-1]:
                self._board[x,y] = i
                


    def updateGoalList(self, player_no, player_list):
        if self.goalList[player_no-1] in self.playerlist[player_no-1]:
            print('found')
            self.goalList[player_no-1] = player_list[0][random.randint(0, 9)] 

           

        
        #playerhomes = self.player1 + self.player2 + self.player3 + self.player4 + self.player5 + self.player6
        #for y, x in playerhomes:
        #    self._board[x,y] = 'x'

    #def init_players(self):
    #    self.players += 1
    #    for y, x in self.player1:
    #        self._board[x,y] = '1'

    # Find all possible moves for a single piece
    def get_possible_moves(self, target, recCall=False):
        possible_moves = []
        jump_pos = []
        jump_pos.append(target)

        while(len(jump_pos) > 0):
            piece = jump_pos.pop(0)
            # Left up
            x = piece[0] - 1
            y = piece[1] - 1
            if(x >= 0 and y >= 0 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x >= 0 and y >= 0 and self._board[x,y] > 0):
                x = piece[0] - 2
                y = piece[1] - 2
                if(x >= 0 and y >= 0 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])

            # Left down
            x = piece[0] - 1
            y = piece[1] + 1
            if(x >= 0 and y <= 16 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x >= 0 and y <= 16 and self._board[x,y] > 0):
                x = piece[0] - 2
                y = piece[1] + 2
                if(x >= 0 and y <= 16 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])

            # Left
            x = piece[0] - 2
            y = piece[1]
            if(x >= 0 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x >= 0 and self._board[x,y] > 0):
                x = piece[0] - 4
                if(x >= 0 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])

            # Right up
            x = piece[0] + 1
            y = piece[1] - 1
            if(x <= 24 and y >= 0 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x <= 24 and y >= 0 and self._board[x,y] > 0):
                x = piece[0] + 2
                y = piece[1] - 2
                if(x <= 24 and y >= 0 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])

            # Right down
            x = piece[0] + 1
            y = piece[1] + 1
            if(x <= 24 and y <= 16 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x <= 24 and y <= 16 and self._board[x,y] > 0):
                x = piece[0] + 2
                y = piece[1] + 2
                if(x <= 24 and y <= 16 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])

            # Right
            x = piece[0] + 2
            y = piece[1]
            if(x <= 24 and self._board[x,y] == 0 and recCall== False):
                possible_moves.append([x,y])
            #Position was occupied. Check if we can jump it instead
            elif(x <= 24 and self._board[x,y] > 0):
                x = piece[0] + 4
                if(x <= 24 and self._board[x,y] == 0 and [x,y] not in possible_moves):
                    jump_pos.append([x,y])
                    possible_moves.append([x,y])
            recCall=True

            

            #Recursive call to find all positions we can jump to
            #if(len(jump_pos) > 0):
            #    print("Piece: ", piece)
            #    print("Possible moves len: ", possible_moves)
            #    for i in range(len(jump_pos)):
            #        possible_moves = possible_moves + self.get_possible_moves(jump_pos[i], recCall=True)
            
        return possible_moves
    

    def updateBoard(self, player, piece, move, index): #Updates the moved piece in playerlist 
        self._board[piece[0],piece[1]] = 0
        self._board[move[0],move[1]] = player+1
        self.playerlist[player][index] =  [move[0],move[1]]
        
        

    
