print("Hello")
print('Hello')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings
# You can use three double quotes:
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Or three single quotes:
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

# Strings are Arrays

# Get the character at position 1 (remember that the first character has the position 0):
d = "Hello, World!"
print(d[1])

# Looping Through a String
for e in "banana":
    print(e)

# String Length
f = "Hello, World!"
print(len(f))

# Check String
txt = "The best things in life are free!"
print("free" in txt)
# Use it in an if statement:
txt1 = "The best things in life are free!"
if "free" in txt1:
    print("Yes, 'free' is present.")


# Check if NOT
txt2 = "The best things in life are free!"
print("expensive" not in txt2)
# Use it in an if statement:
txt3 = "The best things in life are free!"
if "expensive" not in txt3:
    print("No, 'expensive' is NOT present.")
