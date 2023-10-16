#excercise 1
'''Question 1. List Manipulation: Create a list name Numbers containing the integers from 1 to 10.
Perform the following task:-
Print the list.
Add the number 11 to the end of the list.
Insert the number zero at the beginning of the list.
Remove the number 5 from the list.
Print the modified list.'''
numbers=list(range(1,11))
print("List : ",numbers)
numbers.append(11)
numbers.insert(0,0)
del numbers[5]
print("Modified List : ",numbers)
