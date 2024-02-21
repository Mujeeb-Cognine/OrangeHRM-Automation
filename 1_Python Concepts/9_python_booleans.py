# In programming, you often need to know if an expression is True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Check if an object is an integer or not:
j = 200
print(isinstance(j, int))
