#EXPERIMENT 3
s="Welcome to Python world"
siz=len(s)
print("The string is : ",s)
loop=True
while (loop):
    print("Choose option:\n1. Count the number of alphabets in the given string\n2. To extract characters from the string\n3. Check if the string is alphanumeric or not\n4. Exit")
    choice=int(input("Enter: "))
    print("\n")
    if(choice==1):
        count=0
        for i in s:
            if i.isalpha():
                count+=1
        print("The number of alphabets in the given string are: ",count,"\n")
    elif(choice==2):
       print("Which word you want to extract?\n")
       ch=(input("Enter: "))
       if(ch=='Welcome'):
           print("Character: ",s[0:7],"\n")
       elif(ch=='to'):
           print("Character: ",s[8:10],"\n")
       elif(ch=='Python'):
           print("Character: ",s[11:17],"\n")
       elif(ch=='world'):
           print("Character: ",s[18:23],"\n")
       else:
           print("INVALID","\n")
    elif(choice==3):
        if(s.isalnum()):
            print("The string is alphanumeric.","\n")
        else:
            print("The string is not alphanumeric.","\n")
    elif(choice==4):
        loop=False
        print("END","\n")
    else:
        print("Invalid choice","\n")
    
