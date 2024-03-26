def MatrixPrinter(mat):
    for i in mat:
        print(*i,sep = " ")

def userinput():
    m = int(input("Enter the number of rows : "))
    n = int(input("Enter the number of columns : "))
    lst = []
    print("Enter the values row vice ")
    for i in range(1,m+1):
        lst.append(list(eval(input("Enter the row {} separated by commas : ".format(i)))))
    return lst


def addition():
    mat1 = userinput()
    mat2 = userinput()
    NewMatrix = []
    r = 0
    for i in mat1:
        c = 0
        temp = []
        for j in i:
            temp.append(j+mat2[r][c])
            c+=1
        NewMatrix.extend([temp])
        r+=1
    return NewMatrix

            
def subraction():
    mat1 = userinput()
    mat2 = userinput()
    NewMatrix = []
    r = 0
    for i in mat1:
        c = 0
        temp = []
        for j in i:
            temp.append(j-mat2[r][c])
            c+=1
        NewMatrix.extend([temp])
        r+=1
    return NewMatrix

def multiplication():
    mat1 = userinput()
    mat2 = userinput()
    res = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            Sum = 0
            for k in range(len(mat2)):
                Sum += mat1[i][k] * mat2[k][j]
            row.append(Sum)
        res.append(row)
    return res

def determinant():
    mat = userinput()
    r1 = mat[0]
    r2 = mat[1]
    r3 = mat[2]
    determinant = r1[0] * ( r3[2]* r2[1] - r2[2] * r3[1]) - r1[1] * (r3[2] * r2[0] - r3[0] * r2[2]) + r1[2] * (r3[1] * r2[0] - r3[0] * r2[1])
    return determinant


