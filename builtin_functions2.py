#all
l1=[True,True,False]
l2=[True,True,True]
print(all(l1))
print(all(l2))

#any
l3=[True,True,False]
l4=[False,False,False]
print(any(l3))
print(any(l4))

#ascii- returns a string containing a printable representation of an object, NOT ascii value.
print(ascii("Kot, \nBhalwal!"))

#ord-returns the unicode code point of the character
print(ord('a'))
print(ord(' '))
print(ord(','))
print(ord('*'))
print(ord('A'))

print("\n")
print("\n")
print("\n")

#bin- gives binary
print(bin(10))
print(bin(15))

#bool
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1,2]))

#bytearray- returns a mutable bytearray object from an iterable of int
byte_arr=bytearray([65,66,67])
print(byte_arr)
byte_arr[0]=88
print(byte_arr)

#bytes- returns an immutable bytes object from an iterable of int
byte_st=bytes([68,69,70])
print(byte_st)
#byte_st[0]=89
#print(byte_st)

#callable- returns true if object appears callable(can be called as a function),otherwise false
def fun():
    return 42
print(callable(fun))
print(callable(42))
