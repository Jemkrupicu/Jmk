# Create a tuple a which contains the first four positive integers
#  and a tuple b which contains the next four positive integers.
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

# Create a tuple c which combines all the numbers from a and b in any order.
c = a + b

# Create a tuple d which is a sorted copy of c.
d = sorted(c)

# Print the third element of d.
print(d[2])

# Print the last three elements of d without using its length.
print(d[-3:])

# Print the length of d.
print(len(d))
