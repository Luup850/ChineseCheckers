import numpy as np
# Find all possible moves for a single piece
def get_possible_moves(self, piece, jumpPos=False):
    possible_moves = []
    jump_pos = []

    # Left up
    x = piece[0] - 1
    y = piece[1] - 1
    if(x >= 0 & y >= 0 & self._board[x,y] == 0 & jumpPos == False):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x >= 0 & y >= 0 & self._board[x,y] > 0):
        x = piece[0] - 2
        y = piece[1] - 2
        if(x >= 0 & y >= 0 & self._board[x,y] == 0):
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    # Left down
    x = piece[0] - 1
    y = piece[1] + 1
    if(x >= 0 & y <= 16 & self._board[x,y] == 0):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x >= 0 & y <= 16 & self._board[x,y] > 0):
        x = piece[0] - 2
        y = piece[1] + 2
        if(x >= 0 & y <= 16 & self._board[x,y] == 0):
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    # Left
    x = piece[0] - 2
    y = piece[1]
    if(x >= 0 & self._board[x,y] == 0):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x >= 0 & self._board[x,y] > 0):
        x = piece[0] - 4
        if(x >= 0 & self._board[x,y] == 0)
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    # Right up
    x = piece[0] + 1
    y = piece[1] - 1
    if(x <= 24 & y >= 0 & self._board[x,y] == 0):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x <= 24 & y >= 0 & self._board[x,y] > 0):
        x = piece[0] + 2
        y = piece[1] - 2
        if(x <= 24 & y >= 0 & self._board[x,y] == 0):
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    # Right down
    x = piece[0] + 1
    y = piece[1] + 1
    if(x <= 24 & y <= 16 & self._board[x,y] == 0):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x <= 24 & y <= 16 & self._board[x,y] > 0):
        x = piece[0] + 2
        y = piece[1] + 2
        if(x <= 24 & y <= 16 & self._board[x,y] == 0):
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    # Right
    x = piece[0] + 2
    y = piece[1]
    if(x <= 24 & self._board[x,y] == 0):
        possible_moves.append([x,y])
    #Position was occupied. Check if we can jump it instead
    elif(x <= 24 & self._board[x,y] > 0):
        x = piece[0] + 4
        if(x <= 24 & self._board[x,y] == 0):
            jump_pos.append([x,y])
            possible_moves.append([x,y])

    if(len(jump_pos) > 0):
        for i in range(len(jump_pos)):
            get_possible