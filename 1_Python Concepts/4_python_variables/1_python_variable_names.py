# Creating Variables

# No command for declaring variables
x = 5
y = "Mujeeb"
print(x)
print(y)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

z = 4  # x is of type int
z = "Sally"  # x is now of type str
print(z)

# If you want to specify the data type of variable, this can be done with casting.
j = str(3)  # j will be '3'
i = int(3)  # i will be 3
s = float(3)  # s will be 3.0

# You can get the data type of variable with the type() function.
m = 5
n = "Mujeeb"
print(type(m))
print(type(n))

# String variables can be declared either by using single or double quotes:

k = "Mujeeb"
# is the same as
l = 'Mujeeb'

# Variable names are case-sensitive.
a = 4
A = "Mujeeb"
# A will not overwrite a
print(a)
print(A)
