import numpy as np
import math
import board

class AI:
    player_no = 0
   
    def __init__(self, player_no):
        self.player_no = player_no-1
        
        
        
    def findCost(self, piece, goal): #The euclidean distance between a piece location and the goal location 
        cost = math.sqrt(math.pow((goal[0] - piece[0])/2,2) + math.pow(goal[1] - piece[1],2))
        return cost
    
    def findCostChange(self, pos1, pos2, board): #The difference between a piece location and an updated piece location
        return self.findCost(pos1, board.goalList[self.player_no]) - self.findCost(pos2, board.goalList[self.player_no])
    
    
    def findOptimalMove(self, board): #Finds the optimal move by searching for the move that will result in highest cost decrease.
        tmp = 0
        selected_move = None
        piece = [2]
        index = 0
        for i,p in enumerate(board.playerlist[self.player_no]):
            moves = board.get_possible_moves(p)          
            for j in moves:
                change = self.findCostChange(p, j, board)
                if tmp<change:
                    tmp = change
                    selected_move = j
                    piece = p
                    index = i
                    
                elif tmp == change: #If two possible moves result in the same cost change, move the piece with higher initial cost.
                    if (self.findCost(p, board.goalList[self.player_no]) > 
                        self.findCost(piece, board.goalList[self.player_no])):
                       tmp = change
                       selected_move = j
                       piece = p
                       index = i 
                       
        
            
                    
        return piece, selected_move, index
            
    def turn(self, board):
        a,b,c = self.findOptimalMove(board)
        board.updateBoard(self.player_no, a, b, c)
        return board
        
        
        