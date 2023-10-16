l1=[[5,3,2],[8,6,3],[3,5,2],
    [3,6],[3,7,4],[2,9]]
print("The original list is: "+str(l1))
print()
k=int(input("Enter row you want to reverse: "))
print()
res=[]
for i,ele in enumerate(l1):
    if(i+1)%k==0:
        res.append(list(reversed(ele)))
    else:
        res.append(ele)
print("After reversing every kth row: "+str(res))
