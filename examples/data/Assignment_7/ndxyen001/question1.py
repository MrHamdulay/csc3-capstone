# Yentl Naidu (NDXYEN001)
# 29 April 2014
# Assignment 7
# Question 1

# Create empty list
s = []

# Get the input
strings = input("Enter strings (end with DONE):\n")

# Create loop to get the list of strings with a sentinel 
x = 0
while strings != 'DONE': 
    s.append(strings)
    strings = input('')
    if (len(strings)) <= 10:
        x = len(strings)
    else:
        break

# Start with zero counts
count = []

# Count strings and add new strings as they are encountered
for strings in s:
    if not strings in count:
        count.append(strings)
    else:
        continue
   
# Print a statement showing the new list       
print("\nUnique list:")

# Print out the strings only once without repetition
for strings in count: 
    print (strings) # Don't print the number of strings
        