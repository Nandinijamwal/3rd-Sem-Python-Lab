#single quotes
st1='Hello, this is my sentence with single quotes'
print("This is  my sentence with single quotes :")
print(st1)
#double quotes
st2="Python is my fav. programming language"
print("\nString with double quotes : ")
print (st2)
print(type(st2))
#triple quotes
st3='''This a triple quotes string
spreaded over multiple lines.
It can hold 'single' and "double" quote words without escaping.'''
print("\nString with use of triple quotes: ")
print(st3)
print(type(st3))
#multilined
st4='''Strings
     whose
     words
     are
     multilined'''
print("\n Creating multilined string :")
print(st4)
#concatination
st5=st1+ "NEW ONE BEGINS" +st2
print("Concatenated string: ")
print(st5)

