def userinput():
    m = int(input("Enter the number of rows : "))
    n = int(input("Enter the number of columns : "))
    lst = []
    print("Enter the values row vice ")
    for i in range(1,n+1):
        lst.append(list(eval(input("Enter the row {} separated by commas : ".format(i)))))
    return lst


def Cyclic_Generator():
    mat = userinput() 
    comb1 =[[],[],[]]
    comb2 =[[],[],[]]
    comb1[0] = mat[0]
    comb1[1] = [mat[0][1],mat[0][2],mat[0][0]]
    comb1[2] = [mat[0][2],mat[0][0],mat[0][1]]
    comb2[0] = mat[0]
    comb2[2] = [mat[0][1],mat[0][2],mat[0][0]]
    comb2[1] = [mat[0][2],mat[0][0],mat[0][1]]
    return mat,comb1,comb2

def verify():
    mat,comb1,comb2 = Cyclic_Generator()
    if comb1 == mat or comb2 == mat:
        print("The matrix is cyclic.")
    else:
        print("The matrix is not cyclic.")
verify()
