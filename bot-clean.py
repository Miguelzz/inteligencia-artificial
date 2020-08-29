
def position(grid):
    pos=()
    for i in range(5):
        if(pos): break
        for j in range(5):
            if(grid[i][j]=='d'):
                pos = (i, j)
                break
    return pos



def next_move(br, bc, grid):
    dr, dc = position(grid)
    print(dr, dc)
    result = ''
    if(dc == bc and dr == br): result = 'CLEAN'

    if(br > dr): result = 'UP'
    elif(br < dr): result = 'DOWN'

    if(bc > dc): result = 'LEFT'
    elif(bc < dc): result = 'RIGHT'
    print(result)
    



grid = ['-d---', '-d---', '---d-', '---d-', '--d-d' ]
n = 5
r,c = [0,1]


print(next_move(r,c,grid))