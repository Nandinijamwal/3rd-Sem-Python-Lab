#pass by value
a=20
def change(a):
    a=10
    print("The value of a in function: ",a,"and adressed is: ",id(a))
    return a
print("The value of a before: ",a,"and adressed is: ",id(a))
a=change(a)
print("The value of a after: ",a,"and adressed is: ",id(a))

print("\n")
print("*"*20)
print("\n")

#pass by value
l=[1,2,3,4,5,6]
def ch(l):
    l[0]=30
    print("The value of list in function: ",l,"and adressed is: ",id(l))
    return
print("The value of list before: ",l,"and adressed is: ",id(l))
ch(l)
print("The value of list after: ",l,"and adressed is: ",id(l))
