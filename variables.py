#Understand variables assignment and mutability in Python
a = [1,2,3,4,5]

#
b=a
b.append(6)

# b is a name tag for a single memory instance, not a second variable
print(a)  # Output: [1, 2, 3, 4, 5, 6]


c = [1,2,3,4,5,6]
print(a == c)  # Output: True
print (a is c)  # Output: False


# Immutable types: Int, str, tuple, frozenset, bytes
# Mutable types: list, dict, set, bytearray