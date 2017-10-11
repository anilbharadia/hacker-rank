#!/bin/python
def displayPathtoPrincess(n,grid):
    step_count = n // 2
    
    if grid[0][0] == 'p': # Upper Left
        move(step_count, "UP", "LEFT")

    elif grid[0][n-1] == 'p': # Upper Right
        move(step_count, "UP", "RIGHT")
    
    elif grid[n-1][0] == 'p': # lower left
        move(step_count, "DOWN", "LEFT")
    
    elif grid[n-1][n-1] == 'p': # Lower Right
        move(step_count, "DOWN", "RIGHT")

m = input()

def move(n, move1, move2):
    for i in xrange(n):
        print move1
        print move2

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
