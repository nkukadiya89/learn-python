# Variables

Count = 1000
print("variable :",Count)

# DataTypes / Primitive Types

# Text Type:	str

x = "Hello World"
print("str :", x)

# Numeric Types:	int, float, complex
a = 10
print("int :",a)
b=1.4
print("float :",b)
c=5j
print("complex :",c)

# Sequence Types:	list, tuple, range

#list

d = ["Nirav","P","Kukadiya"]
print("List :",d)
print("type of d",type(d)) 

#tuple

e = ("tuple","example")
print("tuple", e)

#range

f = range(2,100)
print("range",f)

# Mapping Type:	dict

g={"Name":"John","Age":"30"}
print("dict :",g)

# Set Types:	set, frozenset

#set

h={"Cycle","byk","car"}
print("set : ", h)

#frozenset

i = frozenset({"google","Yahoo","Bing"})
print("Frozenset :",i)

# Boolean Type:	bool

j = True
print("boolean :",j)

# Binary Types:	bytes, bytearray, memoryview

k=b"Hello World"
print("bytes :",k)

#bytearray
L= bytearray(5)
print("bytearray : ", L)

#memoryView
M= memoryview(bytes(5))
print("memoryview : ", M)
