marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29}

colours = list(marbles)  # the keys will be used by default
counts = tuple(marbles.values())  # but we can use a view to get the values
marbles_set = set(marbles.items())  # or the key-value pairs

print(colours)
print(counts)
print(marbles_set)

list_with_letters = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

s = "".join(list_with_letters)
print(s)

animals = ('cat', 'dog', 'fish')

# a space-separated list
print(" ".join(animals))

# a comma-separated list
print(",".join(animals))

# a comma-separated list with spaces
print(", ".join(animals))

print("cat    dog fish\n".split())
print("cat|dog|fish".split("|"))
print("cat, dog, fish".split(", "))
print("cat, dog, fish".split(", ", 2))

# Convert a list which contains the numbers 1, 1, 2, 3 and 3,
# and convert it to a tuple a.
a = [1, 1, 2, 3, 3]
tuple(a)

# Convert a to a list b. Print its length.
b = list(a)
print(len(b))

# Convert b to a set c. Print its length.
c = list(b)
print(len(c))

# Convert c to a list d. Print its length.
d = list(c)
print(len(d))

# Create a range which starts at 1 and ends at 10. Convert it to a list e.
e = list(range(1, 11))
print(e)

# Create the directory dict.
# Create a list t which contains all
# the key-value pairs from the dictionary as tuples.
directory = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}

t = directory.items()

# Create a list v of all the values in the dictionary.
v = directory.values()

# Create a list k of all the keys in he dictionary.
k = directory.keys()

# Create a string s which contains the word "antidisestablishmentarianism".
# Use the sorted function on it. What is the output type?
# Concatenate the letters in the output to a string s2.
s = "antidisestablishmentarianism"
s1 = sorted(s)

s2 = "".join(s1)
print(s2)

# Split the string "the quick brown fox jumped over the lazy dog"
#  into a list w of individual words.
c_string = "the quick brown fox jumped over the lazy dog"
w = c_string.split(" ")

print(w)