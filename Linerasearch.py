l1=[1,2,3,4,5,77,7,8,86,100]
print("List: ", l1)
tar=int(input("Target: "))
if tar in l1:
    print("Element Found")
    for i in range(len(l1)):
        if l1[i]==tar:
            print("Index: ", i)
else:
    print("Element not Found")

