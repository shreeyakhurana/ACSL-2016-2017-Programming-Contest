"""
Shreeya Khurana
Int 4
"""
import copy

input1 = input("1. ")
input1list = input1.split(", ")

##Create 4x4 grid##
grid = [[0 for i in range(4)]for j in range(4)]
##Create 2 clues for each row##
clues = [[[0, 0] for i in range(4)]for j in range(2)]
for i in range(4):
    clues[1][i][0] = input1list[0][i]
    clues[1][i][0] = int(clues[1][i][0])
    clues[1][i][1] = input1list[5][i]
    clues[1][i][1] = int(clues[1][i][1])
for i in range(1, 5):
    b = input1list[i]
    if len(b) == 2:
        clues[0][i-1][0] = b[0]
        clues[0][i-1][0] = int(clues[0][i-1][0])
        clues[0][i-1][1] = b[1]
        clues[0][i-1][1] = int(clues[0][i-1][1])
    else:
        clues[0][i-1][0] = b[0]
        clues[0][i-1][0] = int(clues[0][i-1][0])
        clues[0][i-1][1] = b[5]
        clues[0][i-1][1] = int(clues[0][i-1][1])
        for j in range(1, 5):
            grid[i-1][j-1] = b[j]
            grid[i-1][j-1] = int(grid[i-1][j-1])

##Finds number of towers       
def numTowers(towers):
    height = 0
    n = 0
    for towerheight in towers:
        if towerheight > height:
            n = n + 1
            height = towerheight
    return n

#Checks if solved
def is_solved(grid):
    for i in range(4):
        row = grid[i]
        if numTowers(row) != clues[0][i][0]:
            return False
        switched_row = reversed(row)
        if numTowers(switched_row) != clues[0][i][1]:
            return False
        column = [grid[j][i] for j in range(4)]
        if numTowers(column) != clues[1][i][0]:
            return False
        switched_column = reversed(column)
        if numTowers(switched_column) != clues[1][i][1]:
            return False
    return True
            
##Finds openings in the grid##
def empty(grid):
    for i in range(4):
        find = grid[i]
        if 0 in find:
            return (i, find.index(0))
    return None

##Solves the game##
def solveGame(grid):
    grid = copy.deepcopy(grid) 
    if empty(grid) is None:
        return (is_solved(grid), grid)
    i, j = empty(grid)
    badHeights = set()
    for a in range(4):
        badHeights.add(grid[a][j])
    for a in grid[i]:
        badHeights.add(a)
    goodHeights = {1, 2, 3, 4}
    possibleSolutions = goodHeights - badHeights
    for a in possibleSolutions:
        grid[i][j] = a
        completed, solvedGame = solveGame(grid)
        if completed:
            return (True, solvedGame)
    return (False, grid)
completed, solvedGame = solveGame(grid)

print("OUTPUTS")
count = 2
for x in range(5):
    print(count)
    i, j = map(int, list(input()))
    print(solvedGame[i-1][j-1])
    print()
    count = count + 1
