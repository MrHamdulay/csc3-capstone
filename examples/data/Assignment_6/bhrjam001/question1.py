# James Behr
# 2014-04-23
# Assignment 6 Question 1

names = [] # list to hold names
print('Enter strings (end with DONE):')
# Loop until sentinel is reached
while True:
    s = input()
    if s == 'DONE':
        break
    names.append(s)
    
# Find longest length with list comprehension, then max() it
try:
    biggest = max([len(name) for name in names])
except ValueError:
    pass

print() # Blank line between input and output
print('Right-aligned list:')
for name in names:
    # Create a format string with a variable 'width' parameter, right-aligned
    formatstr = '{:>' + str(biggest) + '}' 
    print(formatstr.format(name))