# Yentl Naidu (NDXYEN001)
# 23 April 2014
# Assignment 6
# Question 1

# Create empty list
s = []

# Get the input
strings = input("Enter strings (end with DONE):\n")

# Create loop to get the list of strings with a sentinel 
x = 0
while strings != 'DONE': 
    s.append(strings)
    if (len(strings))> x:
            x = len(strings)    
    strings = input('')
    
    
# Print a statement showing the alignment    
print("\nRight-aligned list:")    

# Right align the list
for strings in s:
    print("{0:>{1}}".format(strings,x))
    
    





    