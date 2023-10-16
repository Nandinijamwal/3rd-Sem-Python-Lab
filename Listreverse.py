L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
print(L1)
ch=int(input("Enter row to reverse: "))
#for r,val in enumerate(L1):
if(ch==1):
    L1[0].reverse()
    print(L1[0])
elif(ch==2):
    L1[1].reverse()
    print(L1[1])
elif(ch==3):
    L1[2].reverse()
    print(L1[2])
elif(ch==4):
    L1[3].reverse()
    print(L1[3])
else:
    print("INVALID OP")
#print(L1)
