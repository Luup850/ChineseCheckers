import numpy as np
import math
import board
class AI:
    player_no = 0
    def __init__(self, player_no):
        self.player_no = player_no
        
        
        
        
    def findCost(self, piece, goal):
        cost = math.sqrt(math.pow((goal[0] - piece[0])/2,2) + math.pow(goal[1] - piece[1],2))
        return cost
    
    def findCostChange(self, pos1, pos2):
        return self.findCost(pos1) - self.findCost(pos2)
    
    
    def findOptimalMove(self, board):
        tmp = 0
        selected_move = None
        piece = [2]
        for i,p in enumerate(board.playerlist[self.player_no]):
            moves = board.get_possible_moves(p)          
            for j in moves:
                change = self.findCostChange(p, j)
                if tmp<change:
                    tmp = change
                    selected_move = j
                    piece = p
        
        return piece, selected_move;
            
    
    