import os
def turn(grid,way,from_coord,to_coord):
    [x1,y1] = [int(i) for i in from_coord.split(',')]
    [x2,y2] = [int(i) for i in to_coord.split(',')]
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if way == 'on':
                grid[x][y] = True
            elif way == 'off':
                grid[x][y] = False
            else:
                grid[x][y] = not grid[x][y]
    return
def turn2(grid,way,from_coord,to_coord):
    [x1,y1] = [int(i) for i in from_coord.split(',')]
    [x2,y2] = [int(i) for i in to_coord.split(',')]
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if way == 'on':
                grid[x][y] += 1
            elif way == 'off':
                if grid[x][y]>0:
                    grid[x][y] = grid[x][y]-1
                else:
                    grid[x][y] = 0
                
            else:
                grid[x][y] += 2
    return
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    rows = 1000
    cols = 1000

    # Initialize a 2D array with False values
    grid = [[False for _ in range(cols)] for _ in range(rows)]
    grid2 = [[0 for _ in range(cols)] for _ in range(rows)]
    
    
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            line_par = line.split(' ')
            mode = 'toggle'
            from_coord = 1
            to_coord = 3
            if line_par[0] == 'turn':
                mode = line_par[1]
                from_coord += 1
                to_coord += 1
            turn(grid,line_par[1],line_par[from_coord],line_par[to_coord])
            turn2(grid2,line_par[1],line_par[from_coord],line_par[to_coord])
                
          
    counter = 0
    for line in grid:
        for field in line:
            if field:
                counter+=1 
    counter2 = 0
    for line in grid2:
        for field in line:
            counter2+=field
    print(counter,counter2)
    