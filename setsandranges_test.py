# Create a set a which contains the first four positive integers and
#  a set b which contains the first four odd positive integers.
a = {1, 2, 3, 4}
b = {1, 3, 5, 7}

# Create a set c which combines all the numbers which are in a or b (or both).
c = a | b

# Create a set d which contains all the numbers in a but not in b.
d = a - b

# Create a set e which contains all the numbers in b but not in a.
e = b - a

# Create a set f which contains all the numbers which are both in a and in b.
f = a & b

# g which contains all the numbers which are either in a or in b but not both
g = a ^ b

# Print the number of elements in c.
print(len(c))

# Create a range a which starts from 0 and goes on for 20 numbers.
a1 = list(range(0, 20))

# Create a range b which starts from 3 and ends on 12.
b1 = list(range(3, 13))

# Create a range c which contains every third integer starting from 2 and
# ending at 50.
c1 = list(range(2, 50, 3))
