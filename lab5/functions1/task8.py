mylist=[int(m) for m in input().split()]
def Solve(mylist):
    mylist0=[]
    for a in mylist:
        if a==0 or a==7:
            mylist0.append(a)
    if mylist0[0]==0 and mylist0[1]==0 and mylist0[2]==7:
        print(True)
    else:
        print(False)

cnt=Solve(mylist)
            