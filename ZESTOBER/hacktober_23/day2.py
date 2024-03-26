# You have a 2D grid representing a spider's web. The grid consists of cells where each cell is either empty (0) or contains a spider (1). The spider wants to move from the top-left corner (cell [0][0]) to the bottom-right corner (cell [n-1][m-1]) of the grid while avoiding spiders. The spider can only move right or down to adjacent cells.
# Write a function that determines whether the spider can reach the bottom-right corner of the grid while avoiding spiders. Return True if the spider can reach the end, and False otherwise.

lst = [[0,0,0,0,0],
       [0,1,0,0,1],
       [0,0,1,1,0],
       [0,1,1,0,0],
       [0,0,0,0,0]]

start = (0,0)

path=[]
path_rep = []

def matrix_printer(test):
    for i in range(len(test)):
        for j in range(len(test)):
            test[i][j]= str(test[i][j])
    for i in ((test)):
        for j in i:
            f = len(j)
            if f ==2:
                x=j+' '
            elif f==1:
                x=" "+j+" "
            print(x, end= " ")
        print()
        
        
def right():
    global start
    if(lst[start[0]][start[1]+1] == 0):
        start = (start[0],start[1]+1)
        path.append(start)
        path_rep.append(start)
        return True
    else:
        return False

def bottom(rem = 0):
    global start
    if(rem == 1):
        del path_rep[len(path_rep)-2]
    if(lst[start[0]+1][start[1]] == 0):
        start = (start[0]+1,start[1])
        path.append(start)
        path_rep.append(start)
        return True
    else:
        return False

def exist(s):
    if((s[0]<len(lst) and s[0]>=0) and (s[1]<len(lst) and s[1]>=0)):
        return True
    else:
        return False
    

def spiders():
    global start
    while(True):
        # print(path)
        if(exist((start[0],start[1]+1)) and right()):
            right()
        elif(exist((start[0]+1,start[1])) and bottom()):
            bottom()
        else:
            print(path)
            start = path[len(path)-1]
            path.pop()
            if(exist((start[0]+1,start[1])) and bottom()):
                bottom(1)
# try:
spiders()
print(path_rep)
# except(Exception):
#     matrix_printer(lst)
#     print(path_rep)

