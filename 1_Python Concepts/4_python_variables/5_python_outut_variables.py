# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
m = "Python"
y = "is"
z = "awesome"
print(m, y, z)

# You can also use the + operator to output multiple variables:
n = "Python "
o = "is "
p = "awesome"
print(n + o + p)

# For numbers, the + character works as a mathematical operator:
a = 5
b = 10
print(a + b)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# k = 5
# l = "Mujeeb"
# print(k + l)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
k = 5
l = "Mujeeb"
print(k, l)