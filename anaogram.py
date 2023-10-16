st=input("Enter string 1: ")
st2=input("Enter string 2: ")
if(len(st)!=len(st2)):
    print("No")
else:
    s1=sorted(st)
    s2=sorted(st2)
    print(s1,s2)
    if(s1==s2):
        print("yes")
    else:
        print("no")
