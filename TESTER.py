#1.
'''a=input("Your name: ")
b=int(input("Your age: "))
print("Name: ",a, "; Age: ",b)'''

#2.
'''num1=int(input("Enter no.1: "))
num2=int(input("Enter no.2: "))
a=num1+num2
print("ADD: ",a)
s=num1-num2
print("SUB: ",s)
m=num1*num2
print("MULTIPLY: ",m)
d=num1/num2
print("DIV: ",d)
print("MOD: ",num1%num2)'''

#3.
'''r=int(input("Radius: "))
pi=3.14
print("Diameter of the circle = ",2*r)
print("Perimeter of the circle = ", 2*pi*r)
print("Area of the circle= ", pi*r*r)'''

#4.Noadd
'''a=int(input())
b=int(input())
res=b
for i in range(1,a+1):
    res=res+1
print("Result", res)'''

#5.
'''a=int(input())
b=int(input())
res=b
for i in range(1,a):
    res=res+b
print("Result", res)'''

#6.
'''a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print("a: ", a, "b: ",b)'''

#7.
'''a=int(input("ENTER NUMBER:"))
if(a>10):
    print("Greater")
elif(a=10):
    print("Same")
else:
    print("Smaller")'''

#8.
'''a=int(input("ENTER NUMBER:"))
if(a%2==0):
    print("Even")
else:
    print("Odd")'''

#9.
print("MAX NUMBER")
a=int(input("Enter : "))
b=int(input("Enter : "))
c=int(input("Enter : "))
l1=[]
l1.append(a)
l1.append(b)
l1.append(c)
print("List: ",l1)
print("Max: ", max(l1))
