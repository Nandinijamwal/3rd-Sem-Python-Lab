st=input("Enter String: ")
print(st)
length=len(st)
half=length//2
l1=[]
l2=[]
for i in st[half+1:]:
    l1.append(i)
for i in st[half-1::-1]:
    l2.append(i)
print(l1,l2)
if(l1==l2):
    print("PALINDROME")
else:
    print("NOT PALINDROME")



n=input("Enter String: ")
print(n)
r=len(n)+1
l=0
while l<r:
    if n[1]!=n[r]:
        print("no")
    else:
        l+=1
        r-=1
    print("yes")
