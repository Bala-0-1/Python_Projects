def half_diamond(n):
    count = 0
    for i in range(1,n*2):
        if(i>n):
            count-=1
            print(" "*(n-count),"*"*count)
        else:
            count+=1
            print(" "*(n-count),"*"*count)
           
        
def diamond(n):
    count = 1
    spaces = n//2
    for i in range(1,n+1):
        if(i>(n//2)+1):
            count-=2
            spaces+=1
            print(" "*spaces,"*"*count)
        else:
            print(" "*spaces,"*"*count)
            if(i == n//2+1):
                continue
            count+=2
            spaces-=1

diamond(5)