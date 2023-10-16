#CALCULATOR

print("WELCOME TO MY CALCULATOR")

ch=input("1. Simple Calculator\n2. Eligibility Calculator\n ENTER:")
if(ch==1):
    num1=int(input("Num1: "))
    num2=int(input("Num2: "))
    op=int(input("Choose operation:\n 1. +\n 2. -\n 3. *\n 4. /\n 5. %\nEnter:  "))
    if(op==1):
        a=num1+num2
        print("ADD: ",a)
    elif (op==2):
        s=num1-num2
        print("SUB: ",s)
    elif(op==3):
        m=num1*num2
        print("MULTIPLY: ",m)
    elif(op==4):
        d=num1/num2
        print("DIV: ",d)
    elif(op==5):
        print("MOD: ",num1%num2)
    else:
        print("INVALID INPUT")

else:
    s1=int(input("Enter marks in Personality traits: "))
    s2=int(input("Enter marks in Discipline: "))
    s3=int(input("Enter marks in Language Fluency: "))
    total=s1+s2+s3
    print("Total=",total)
    if(total<15):
        print("NOT ELIGIBLE FOR RECRUITMENT")
    elif(total>15):
        if(total<22):
             print("WAITING LIST")
        elif(total==30):
            print("ELIGIBLE! PERFECT SCORE")
        else:
            print("Eligible")
print("********************THANKYOU********************")

