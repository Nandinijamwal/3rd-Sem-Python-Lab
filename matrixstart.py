#matrix
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
for r in L1:
    for c in r:
        print(c,end=" ")
    print()'''


#add
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=0
eve=0
evecount=0
for r in L1:
    for c in r:
        count+=c
        print(c,end=" ")
        if(c%2==0):
            eve+=c
            evecount+=1
    print()
print("total sum: ",count)
print("even sum: ",eve)
print("even count: ",evecount)'''

#second row sum
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=0
for c in L1[1]:
    count+=c       
print("sum: ",count)'''

#add even position no.s
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=for r in L1:
    for i,val in enumerate(r):
        if i%2==0:
            print(val, i)
            count+=val
print("Sum: ",count)'''

#add last column
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=0
for r in L1:
    count+=r[3]
print(count)'''

#add diagonal
'''L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=0
for r in L1:
    for c,val in enumerate(r):
        if(L1[c]+==r):
            count+=val
print(count)'''

#add opp diagonal
L1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
count=0
for r in range(0,len(L1)):
    for c in range(0,len(L1[r])):
        if(r+c==3):
            count+=L1[r][c]
print(count)


