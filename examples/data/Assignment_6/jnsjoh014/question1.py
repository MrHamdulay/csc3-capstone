"""Assignment 6 Question 1
Johan Jansen van Vuuren (JNSJOH014)
21 April 2014"""

# input data
names = []
one_name = input("Enter strings (end with DONE):\n")
while one_name.upper() != "DONE":
    names.append(one_name)
    one_name = input("")

# print list title
print("\nRight-aligned list:")

# get length of longest name
maxLen = 0
for one_name in names:
    if len(one_name)>maxLen:
        maxLen = len(one_name)

# aligned list
for one_name in  names:
    formatString = "{0:>"+str(maxLen)+"}" # Create format string
    temp = formatString.format(one_name)
    print(temp)

