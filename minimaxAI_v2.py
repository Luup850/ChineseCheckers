# function  minimax(node, depth, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, minimax(child, depth − 1, FALSE))
#         return value
#     else (* minimizing player *)
#         value := +∞
#         for each child of node do
#             value := min(value, minimax(child, depth − 1, TRUE))
#         return value


import copy
class MinimaxAI_v2:
    player_no = 0
    current_players = []
    turn_count = 0

    def __init__(self, player_no, current_players):
        self.player_no = player_no-1
        print(self.player_no)
        for p in current_players:
            self.current_players.append(p)

    def take_turn(self, board):
        self.turn_count = self.turn_count + 1
        board.board_name = 'Copy of main'
        origin = Node(None, copy.deepcopy(board._board), copy.deepcopy(board.playerlist), [], 0)
        self.minimax(origin, 1, 3, copy.deepcopy(board))

        max_val = -9999
        best_node_index = 0
        for node in origin.children:
            if(node.value > max_val):
                max_val = node.value
                best_node = node
        #board.update_board(best_node.nodes_move[0], best_node.nodes_move[1])
        print("Player {0}, moved {1} to {2}".format(self.player_no + 1, best_node.nodes_move[0], best_node.nodes_move[1]))
        #print("Nodemoves: ", node.nodes_move)
        return copy.deepcopy(node.nodes_move)

    def minimax(self, node, depth, moves_to_consider, board, maximize=True):
        if(depth == 0):
            return node

        # Maximize
        if(maximize == True):
            best_moves = board.get_best_moves(self.player_no, moves_to_consider)
            for move in best_moves:
                # Save current board so we can restore it
                cur_board = copy.deepcopy(node.board)
                cur_playerlist = copy.deepcopy(node.playerlist)

                board.update_board(move[0], move[1])
                child_node = Node(node, copy.deepcopy(node.board), copy.deepcopy(node.playerlist), move[:2], move[2])
                node.children.append(child_node)
                self.minimax(child_node, depth-1, moves_to_consider, copy.deepcopy(board), False)
                board._board = copy.deepcopy(cur_board)
                board.playerlist = copy.deepcopy(cur_playerlist)

            # Now find the node with the highest gain
            best_val = node.value
            for i,child in enumerate(node.children):
                if(child.value > best_val):
                    best_val = child.value
            node.value = best_val
        
        if(maximize == False):
            # Currently only works with 1 enemy player which is why current_players[0]
            best_moves = board.get_best_moves(self.player_no, self.current_players[0])
            for move in best_moves:
                # Save current board so we can restore it
                cur_board = copy.deepcopy(node.board)
                cur_playerlist = copy.deepcopy(node.playerlist)

                board.update_board(move[0], move[1])
                # The value has been flipped because it impacts the AI negatively that the player gets closer.
                child_node = Node(node, copy.deepcopy(node.board), copy.deepcopy(node.playerlist), move[:2], -move[2])
                node.children.append(child_node)
                self.minimax(child_node, depth-1, moves_to_consider, copy.deepcopy(board), True)
                board._board = copy.deepcopy(cur_board)
                board.playerlist = copy.deepcopy(cur_playerlist)

            # Now find the node with the highest gain
            best_val = node.value
            for i,child in enumerate(node.children):
                if(child.value < best_val):
                    best_val = child.value
            node.value = best_val


class Node:
    parent = object
    board = []
    playerlist = []
    value = 0
    children = []
    nodes_move = []

    def __init__(self, parent, board, playerlist, nodes_move, value):
        self.parent = parent
        self.board = copy.deepcopy(board)
        self.playerlist = copy.deepcopy(playerlist)
        self.nodes_move = nodes_move
        self.value = value
