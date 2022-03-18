from operator import index
import numpy as np
import math
#################################################
#           Useful functions                    #
#################################################
def heuristic_function(start, end):
    return euclidean_distance(start, end)

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def euclidean_distance(start, end):
    return math.sqrt(math.pow(start[0] - end[0], 2) + math.pow((start[1] - end[1]) / 2, 2))

def dynamic_dist(start, end_list, board_array):
    dist = euclidean_distance(start, end_list[0])
    index_list = 0
    for i,end in enumerate(end_list):
        if(board_array[end[0], end[1]] == 0):
            if(dist > heuristic_function(start, end)):
                dist = heuristic_function(start, end)
                index_list = i
    return heuristic_function(start, end_list[index_list])