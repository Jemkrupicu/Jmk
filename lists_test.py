# create a list with odd positive numbers
a = [1, 3, 5]

# create a list with even positive numbers
b = [2, 4, 6]

# combines lists "a" and "b"
c = a+b

# sort list "c" in order withou changing c
d = sorted(c)

# reverse "d"
reverse_d = d[::-1]

# change fourth position in the list to number 42
change_item = c[3] = 42
# c.insert(3,42) insert element to the 4th place in the list

# append 10 to the end of "d"
append_d = d.append(10)

# extend list "c"
extend_c = c.extend([7, 8, 9])

# print the last element of "d" without using its length
last_item_d = d[-1]

# length of d
length_d = len(d)
print(a)
print(b)
print(c)
print(d)
