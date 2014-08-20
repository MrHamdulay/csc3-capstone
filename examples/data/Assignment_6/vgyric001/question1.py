# Assignment 6
# Question 1
# Richard van Gysen
# 21 April 2014
# Enter names
names = input("Enter strings (end with DONE):\n")
lis = []
# Add names
if names!= 'DONE':
    lis.append(names)
long = 0
# Terminate list when DONE is entered
while names!='DONE':
    names = input()
    if names == 'DONE':
        break
    lis.append(names)
if lis ==[]:
    long = 0
else:
    long = len(max(lis, key = len))    
print()  
# Find max length of word in list
print("Right-aligned list:")
# Print each name right-aligned
for names in lis:
    print(names.rjust(long, ' '))