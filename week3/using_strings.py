my_string = "alpha"
multiline_string = """bravo
charlie"""
print(my_string)
print(multiline_string)

print(my_string[0])
print(my_string[3])

print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)

# my_string[0] = "b" // Not possible, as assignment is not supported.

for char in my_string:
    print(char)

print("pha" in my_string) # true
print("z" not in my_string) # true

