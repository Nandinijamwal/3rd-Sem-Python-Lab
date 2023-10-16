"""text = " My , name , is , Anthony , Gonzalvez "
rint(txxt)
txt = text.split( "," )
print(txt)"""

#_______________________________________________________________________


l1 = [1,2,3,4]
l1.append(100)
print(l1)
l2 = [2,3,4,5,6,7,9]
l1.extend(l2)
print(l1)
l3 = [10,20,30,40]
l3.insert(2,20000)
print(l3)


#________________________________________________________________________

l3 = []
size = int(input("Enter the size of list :"))
for i in range(0,size):
    l6 = int(input("Enter the number :"))
    l3.append(l6)
print(l3)
ele = int(input("Enter the element you want to inssert :"))
ind = int(input("Enter the index where you want to inssert the element :"))
l3.insert(ind,ele) 

#________________________________________________________________________

l7=[1,2,3,4,5,6,7,8,9,10]
del l7[0:2]
print(l7)
l7.remove(10)
print(l7)
