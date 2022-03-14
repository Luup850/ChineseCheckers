import numpy as np
import math
import board
import copy

class AI:
    player_no = 0
   
    def __init__(self, player_no):
        self.player_no = player_no-1
        
        
        
    def findCost(self, piece, goal): #The euclidean distance between a piece location and the goal location 
        cost = math.sqrt(math.pow((goal[0] - piece[0])/2,2) + math.pow(goal[1] - piece[1],2))
        return cost
    
    def findCostChange(self, pos1, pos2, board, player_no): #The difference between a piece location and an updated piece location
        return self.findCost(pos1, board.goalList[player_no]) - self.findCost(pos2, board.goalList[player_no])
    
    # def findCostChangeBoard(self, initial_board, updated_board):
    #     sum = 0
    #     for i,p in enumerate(board.playerlist[self.player_no]):
    #         sum += findCostChange()
    
    def findOptimalMove(self, board, player_no): #Finds the optimal move by searching for the move that will result in highest cost decrease.
        player_number = 0
        if player_number == -1 :
            player_number = self.player_no
        else:
            player_number = player_no

        tmp = 0
        selected_move = None
        piece = [2]
        index = 0
        for i,p in enumerate(board.playerlist[player_no]):
            moves = board.get_possible_moves(p)          
            for j in moves:
                change = self.findCostChange(p, j, board, player_no)
                if tmp<change:
                    tmp = change
                    selected_move = j
                    piece = p
                    index = i
                    
                elif tmp == change: #If two possible moves result in the same cost change, move the piece with higher initial cost.
                    if (self.findCost(p, board.goalList[player_no]) > 
                        self.findCost(piece, board.goalList[player_no])):
                       tmp = change
                       selected_move = j
                       piece = p
                       index = i 
                       
    
        return piece, selected_move, index
    
    
    
    
    def chooseMove(self, board, depth, branches=3):
        moves = []
        cost_list = np.zeros((branches))
        for i,p in enumerate(board.playerlist[self.player_no]):
            
            for j in board.get_possible_moves(p):
                moves.append((p, j,self.findCostChange(p, j, board, self.player_no),i))
                
        moves.sort(key=lambda tup: tup[2], reverse = True)
        best_moves = moves[0:branches]
        copied_board = copy.deepcopy(board._board)
        for i,l in enumerate(best_moves):
            board._board = copied_board
            copied_board = copy.deepcopy(board._board)
            board.updateBoard(self.player_no, l[0], l[1],l[3])
            print("L", l[0])
            #print(copied_board._board)
            improvements_other_players = 0 
            for m in range(board.number_of_players): #We assume all players play their turn in a greedy way
                next_player = (m + self.player_no) % board.number_of_players   
                if (next_player != self.player_no):
                    print("Player turn: ", next_player)
                    start_position,end_position,c = self.findOptimalMove(board, next_player)
                    board.updateBoard(next_player, start_position, end_position, c)
                    #self.simulateTurn(copied_board, next_player)
                    improvements_other_players = improvements_other_players + self.findCostChange(start_position, end_position, board, next_player)
                    #print(copied_board._board)
            cost_list[i] = l[2] - improvements_other_players / (board.number_of_players - 1)
        
        board._board = copied_board
        best_move_index = 0
        tmp = cost_list[0]
        for index,c in enumerate(cost_list):
            if(c > tmp):
                best_move_index = index
        return self.player_no, best_moves[best_move_index][0], best_moves[best_move_index][1], best_moves[best_move_index][3]



            
    def simulateTurn(self, board, player_no):
        a,b,c = self.findOptimalMove(board, player_no)
        print(a,b)
        board.updateBoard(player_no, a, b, c)
        return board, a, b
     
    
        
    # I'm trying the minimax algorithm
    # tmp = 0
    # selected_move = None
    # piece = [2]
    # index = 0   
    # counter = 0
    
   
    
    # def chooseMove(self, board, depth):
    #     change_list = np.zeros((3))
    #     change_index_list = np.zeros((3))
    #     for i,p in enumerate(board.playerlist[self.player_no]):
    #         moves = board.get_possible_moves(p)
    #         for t,j in enumerate(moves):
    #             for k,l in enumerate(change_list):
    #                 change = self.findCostChange(p, j, board)
    #                 if change > l:
    #                     change_list[k] = change
    #                     change_index_list[k] = t
    #                     break
    #                     print(change)
    #                     np.append(change_list,change)
    #                     print(change_list)
    #                     np.sort(change_list, axis=0)
    #                     print(change_list)
    #                     best_moves = [change_list[0], change_list[1], change_list[2]]
    #                     print(best_moves)
    #                     if change > 0 :
    #                         copy_board = board.copy()
    #                         tmp = change
    #                         selected_move = j
    #                         piece = p
    #                         index = i 
    #                         copy_board.updateBoard(p, j, i)
                            
    #                         if(depth == 0): #After all iterations are done
                            
    #                             # change = findCostChangeBoard(initial_board, updated_board) #Implement func
    #                             # if change > tmp:
    #                             #     tmp = change
    #                             #     selected_move = j
    #                             #     index = i
                                
    #                             if(j == moves.length()): #After all the moves are checked
    #                                 return piece, selected_move, index
                                
    #                         for l,p in enumerate(board.playerlist): #We assume all players play their turn in a greedy way
    #                             if (l!=self.player_no):
    #                                 p.turnGreedy(board)
                             
                            
                            
    #                         self.chooseMove(self, copy_board, depth-1)    
                    
                    
                            
                
    #     return piece, selected_move, index