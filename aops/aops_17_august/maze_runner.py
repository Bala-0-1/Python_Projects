
test=[  ["S", 0, 1,1, 1,  0,0,1],
        [1,   0, 0,0, 1,  1,1,1],
        [1,   0, 0,0, 0,  0,0,0],
        [1,   0, 1,0,"G", 0,1,1],
        [1,   1, 1,0, 1,  0,0,1],
        [1,   0, 1,0, 1,  1,0,1],
        [1,   0, 0,0, 0,  1,0,1],
        [1,   1, 1,1, 1,  1,1,1]
    ]


'''
 ["S", 0, 1,1, 1,  0,0,1],
        [1,   0, 0,0, 1,  1,1,1],
        [1,   0, 0,0, 0,  0,0,0],
        [1,   0, 1,0,"G", 0,1,1],
        [1,   1, 1,0, 1,  0,0,1],
        [1,   0, 1,0, 1,  1,0,1],
        [1,   0, 0,0, 0,  1,0,1],
        [1,   1, 1,1, 1,  1,1,1]
'''
ideal_output=[[17, 0, 1,1,1,0,0,1],
              [16,0,0,0,1,1,1,1],
              [15,0,0,0,0,0,0,0],
              [14,0,16,0,"G",0,1,11],
              [13,14,15,0,1,0,0,10],
              [12,0,16,0,2,3,0,9],
              [11,0,0,0,0,4,0,8],
              [10,9,8,7,6,5,6,7]]



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


#finds the start point of the maze

def start_finder():
    for i in test:
        if "G" in i:
            start_coordinates = (test.index(i),i.index("G"))
            return start_coordinates
    else:
        return "Wrong maze"

c = list(start_finder())


# Check the existence of the index in the array 

def exist(num):
    if(num[0]<=7 and num[1]<=7) and (num[0]>=0 and num[1]>=0):
        return True
    else:
        return False
    
#checks the neighbouring elements and returns True if the value is 1

def n_check():
    global test
    global c
    left = [c[0],c[1]-1]
    right = [c[0],c[1]+1]
    top = [c[0]-1,c[1]]
    bottom = [c[0]+1,c[1]]
    if exist(left) and test[left[0]][left[1]] == 1:
        return True
    elif exist(right) and test[right[0]][right[1]] == 1:
        return True
    elif exist(top) and test[top[0]][top[1]] == 1:
        return True
    elif exist(bottom) and test[bottom[0]][bottom[1]] == 1:
        return True
    else:
        return False
    
#Checks the neighbouring element and changes their weight

def neighbour_checker():
    global test
    global c
    left = [c[0],c[1]-1]
    right = [c[0],c[1]+1]
    top = [c[0]-1,c[1]]
    bottom = [c[0]+1,c[1]]
    print(c)
    # print(top)
    # print(n_check())
    if exist(left) and test[left[0]][left[1]] == 1:
        test[left[0]][left[1]] = test[left[0]][left[1]+1]+1 
        c = (test.index(test[left[0]]),test[left[0]].index(test[left[0]][left[1]]))
        print(c)
        print("left : ",left)
    if exist(right) and test[right[0]][right[1]] == 1:
        test[right[0]][right[1]] = (test[right[0]][right[1]-1])+1
        c = (test.index(test[right[0]]),test[right[0]].index(test[right[0]][right[1]]))
        print(c)
        print("right : ",right)
    if exist(top) and test[top[0]][top[1]] == 1 and test[top[0]-1][top[1]]!="G" and test[top[0]+1][top[1]]!="S":
        test[top[0]][top[1]] = test[top[0]+1][top[1]]+1
        c = (test.index(test[top[0]]),test[top[0]].index(test[top[0]][top[1]]))
        print(c)
        print("top : ",top)
    if exist(bottom) and test[bottom[0]][bottom[1]] == 1:
        if test[bottom[0]-1][bottom[1]] == "G" and test[bottom[0]][bottom[1]] == 1:
            test[bottom[0]][bottom[1]] = 2
            c = (test.index(test[bottom[0]]),test[bottom[0]].index(test[bottom[0]][bottom[1]]))
        else:    
            test[bottom[0]][bottom[1]] = test[bottom[0]-1][bottom[1]]+1
            c = (test.index(test[bottom[0]]),test[bottom[0]].index(test[bottom[0]][bottom[1]]))
        print(c)
        print("bottom : ",bottom)
        


# Changes the weight recursively

def weight():
    while(n_check()):
        if(test[c[0]-1][c[1]] == "S"):
            test[c[0]-1][c[1]] = test[c[0]+1][c[1]]+2
            break
        neighbour_checker()
      
weight()


matrix_printer(test)

# Finding the Start position

def S_Finder():
    for i in test:
        if "S" in i:
            start = (test.index(i),i.index("S"))
            return start
    else:
        return "Wrong maze"
    

#Finding the optimal path among all the paths
def desc():
    start = S_Finder()
    
    
coords = []
def path_finder():
    start = S_Finder()
    while(True):
        pass


