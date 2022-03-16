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

    def __init__(self, player_no, current_players):
        self.player_no = player_no-1
        for p in current_players:
            self.current_players.append(p)

    def take_turn(self, board):
        origin = Node(None, board._board, board.playerlist)
        self.minimax(origin, 3, 3, board)

    def minimax(self, node, depth, moves_to_consider, board, maximize=True):
        print("bla")


class Node:
    parent = object
    board = []
    playerlist = []
    value = 0
    children = []

    def __init__(self, parent, board, playerlist):
        self.parent = parent
        self.board = copy.deepcopy(board)
        self.playerlist = copy.deepcopy(playerlist)
