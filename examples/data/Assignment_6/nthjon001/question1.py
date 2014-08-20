"""prints out a right-aligned list of names entered by user, until a sentinel is entered
Jonathan Nathan
20 April 2014"""

# create empty list
x_list=[]

# create a variable to append list with
x_append=input("Enter strings (end with DONE):\n")

# create a variable to keep track of the longest string entered
max_length = 0

# appends input to list until 'DONE' is entered
while x_append != "DONE":
    x_list.append(x_append)
    # keeps track of longest string entered
    if len(x_append) > max_length:
        max_length = len(x_append)    
    x_append=input('')


# prints a blank line and heading  
print()
print('Right-aligned list:')

# prints the list of names with right alignment
for i in range(len(x_list)):
    print((max_length-len(x_list[i]))*' ',x_list[i],sep='')