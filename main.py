# import re
# import time

# def position(grid):
#     princess = ()
#     mario = ()
#     for y, r in enumerate(grid):
#         for x, c in enumerate(re.findall(".", r)):
#             if(c in 'p'):
#                 princess = (y, x)
#             elif(c in 'm'):
#                 mario = (y, x)
#     return (princess, mario)



# def displayPathtoPrincess(grid):
#     (princess, mario) = position(grid)
#     x = 0
#     y = 0
#     print(princess, mario) 

#     if(mario[0] > princess[0]):
#         y = -(mario[0] - princess[0])   
#     else:
#         y = princess[0] - mario[0]

#     if(mario[1] > princess[1]):
#         x = -(mario[1] - princess[1])    
#     else:
#         x = princess[1] - mario[1]


#     result = ''
#     if(y > 0):
#         result = 'DOWN\n' * y
#     else:
#         result = 'UP\n' * -y

#     if(x > 0):
#         result += 'RIGHT\n' * x
#     else:
#         result += 'LEFT\n' * -x

#     print(result)
    

# grid = []

# for i in range(9):
#     grid.append('-'*9)

# grid[0] = grid[0][:1] + 'p' + grid[0][2:]
# grid[5] = grid[5][:3] + 'm' + grid[5][4:]
# print(grid)
# start = time.time()
# displayPathtoPrincess(grid)
# end = time.time()
# print(end - start)

import time
def pos(n,grid,c):
    pos=[]
    for i in range(n):
        for j in range(n):
            if(grid[i][j]==c):
                pos.append(i)
                pos.append(j)
                break
    return pos
def displayPathtoPrincess(n,grid):
    p_pos=pos(n,grid,"p")
    m_pos=pos(n,grid,"m")
    while(m_pos[0]!=p_pos[0] or m_pos[1]!=p_pos[1]):
        if(m_pos[0]<p_pos[0]):
            print("DOWN")
            m_pos[0]=m_pos[0]+1
        if(m_pos[0]>p_pos[0]):
            print("UP")
            m_pos[0]=m_pos[0]-1
        if(m_pos[1]>p_pos[1]):
            print("LEFT")
            m_pos[1]=m_pos[1]-1
        if(m_pos[1]<p_pos[1]):
            print("RIGHT")
            m_pos[1]=m_pos[1]+1
grid = []
for i in range(9):
    grid.append('-'*9)
grid[0] = grid[0][:1] + 'p' + grid[0][2:]
grid[5] = grid[5][:3] + 'm' + grid[5][4:]

start=time.time()
displayPathtoPrincess(9,grid)
end=time.time()
print(end-start)

