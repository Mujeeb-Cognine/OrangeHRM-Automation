# Create a variable outside of a function, and use it inside the function
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""
y = "awesome"


def myfunct():
    y = "fantastic"
    print("Python is " + y)


myfunct()

print("Python is " + y)

# The global Keyword
"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""


def my_func():
    global m
    m = "fantastic1"


my_func()

print("Python is " + m)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
k = "awesome"


def myfunc_():
    global k
    k = "fantastic_"


myfunc_()

print("Python is " + k)
