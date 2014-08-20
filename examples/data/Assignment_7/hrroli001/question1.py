# Question 1 - Assignment 7
# Oliver Harrison
# 27 April 2014



# create list
strings = []

# get strings and add to list

x = input("Enter strings (end with DONE):\n")
print()
while x != "DONE":
    strings.append(x)
    x = input("")

# create new list

new_strings = []

# scan through list, add to list without duplicating

for string in strings:
    if string in new_strings:
        continue
    else:
        new_strings.append(string)

# print new list

print("Unique list:")

for string in new_strings:
    print(string)
    