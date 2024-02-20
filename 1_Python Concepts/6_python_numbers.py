# There are three numeric types in Python:
"""
int
float
complex
"""
x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
k = 1
l = 35656222554887711
m = -3255522

print(type(k))
print(type(l))
print(type(m))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
a = 1.10
b = 1.0
c = -35.59

print(type(a))
print(type(b))
print(type(c))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
d = 35e3
e = 12E4
f = -87.7e100

print(type(d))
print(type(e))
print(type(f))

# Complex numbers are written with a "j" as the imaginary part:
g = 3 + 5j
h = 5j
i = -5j

print(type(g))
print(type(h))
print(type(i))

# You can convert from one type to another with the int(), float(), and complex() methods:
j = 1  # int
k = 2.8  # float
l = 1j  # complex

# convert from int to float:
m = float(j)

# convert from float to int:
n = int(k)

# convert from int to complex:
o = complex(l)

print(m)
print(n)
print(o)

print(type(m))
print(type(n))
print(type(o))

# Random Number
import random

print(random.randrange(1, 10))
