l1=[1,2,3,4,33,0,8,6,44,7,899]
print("list: ",l1)
print("Sorted list: ",l1.sort())
x=int(input("Target: "))
low=0
high=len(l1)-1
mid=0
while low<=high:
    mid=(high+low)//2
    if l1[mid] < x:
        low = mid + 1
    elif l1[mid] > x:
        high = mid - 1
    else:
        print("Found at:", mid-1)
        break
