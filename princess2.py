
def position(grid):
    pos = ()
    x, y = [0, 0]

    for r in grid:
        y = 0
        for c in r:
            if(c in 'd'):
                pos = (x, y)
            y += 1
        x += 1
    return pos



def next_move(br, bc, grid):
    dr, dc = position(grid)

    if(dc == bc and dr == br):
        return 'CLEAN'

    if(br > dr):
        return 'UP'
    elif(br < dr):
        return 'DOWN'

    if(bc > dc):
        return 'LEFT'
    elif(bc < dc):
        return 'RIGHT'
    



grid = ['-----', '---d-', '-----', '-----', '--b--' ]
n = 5
r,c = [4,2]


print(next_move(r,c,grid))