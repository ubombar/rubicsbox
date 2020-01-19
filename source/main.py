import collections
import heapq
import random

# This program is for solwing 2x2 rubic's cube!

SOLVED = (0, 1, 2, 3, 4, 5, 6, 7)

MOVES = (   (4, 0, 2, 3, 5, 1, 6, 7), # U
            (0, 1, 6, 2, 4, 5, 7, 3), # D
            (4, 1, 0, 3, 6, 5, 2, 7), # L
            (0, 5, 2, 1, 4, 7, 6, 3), # R
            
            (1, 5, 2, 3, 0, 4, 6, 7), # U'
            (0, 1, 3, 7, 4, 7, 2, 6), # D'
            (2, 1, 6, 3, 0, 5, 4, 7), # L'
            (0, 3, 2, 7, 4, 1, 6, 5)) # R'

MOVEID = ["U", "D", "L", "R", "U'", "D'", "L'", "R'"]

def apply_move(cube, move):
    newone = [0, 1, 2, 3, 4, 5, 6, 7]

    for ci, ni in enumerate(MOVES[move]):
        newone[ci] = cube[ni]
    
    return tuple(newone)

def error_of(cube, solved=SOLVED):
    error = 0

    for first, second in zip(cube, solved):
        error += ((first - second) ** 2) / 64
    
    return error


'''
cube = tuple(range(0, 8))

cube = apply_move(cube, 0)

print(cube)

print(error_of(cube))
'''

def solution(cube, rstate=SOLVED):
    visited = set()
    heap = list()
    distances = collections.defaultdict(lambda: float('inf'))
    previouses = dict()

    heapq.heappush(heap, (0, cube))
    distances[cube] = 0

    while len(heap) != 0:
        distance, current = heapq.heappop(heap)
        error = error_of(current)

        visited.add(current)

        if error == 0:
            break

        for moveid in range(0, 8): # there are 8 different moves possible
            movedcube = apply_move(current, moveid)

            if movedcube in visited:
                del movedcube
                continue

            heuristicdistance = distance + 1 + error

            if distances[movedcube] > heuristicdistance:
                distances[movedcube] = heuristicdistance
                heapq.heappush(heap, (heuristicdistance, movedcube))
                previouses[movedcube] = (current, MOVEID[moveid])
                
    if rstate in visited:
        if rstate not in previouses:
            return ""

        path = str()
        node = rstate

        while True:

            node, movid = previouses[node]
            path = movid + " " + path

            if node == cube:
                break
        
        return path
    return None

random.seed()

cube = (0, 1, 2, 3, 4, 5, 6, 7)

for i in range(4):
    cube = apply_move(cube, random.randint(0, 7))

print(solution(cube))