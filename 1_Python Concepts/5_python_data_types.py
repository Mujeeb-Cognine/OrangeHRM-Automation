# Python has the following data types built-in by default, in these categories:
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Getting the Data Type
x = 5
print(type(x))


# Setting the Data Type
# str
a = "Hello World"
print(type(a))
# int
b = 20
print(type(b))
# float
c = 20.5
print(type(c))
# complex
d = 1j
print(type(d))
# list
e = ["apple", "banana", "cherry"]
print(type(e))
# tuple
f = ("apple", "banana", "cherry")
print(type(f))
# range
g = range(6)
print(type(g))
# dict
h = {"name" : "John", "age" : 36}
print(type(h))
# set
i = {"apple", "banana", "cherry"}
print(type(i))
# frozenset
j = frozenset({"apple", "banana", "cherry"})
print(type(j))
# bool
k = True
print(type(k))
# bytes
l = b"Hello"
print(type(l))
# bytearray
m = bytearray(5)
print(type(m))
# memoryview
n = memoryview(bytes(5))
print(type(n))
# None
o = None
print(type(o))
