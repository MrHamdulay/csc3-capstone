"""Lenard Carroll
21 April 2014
CRRLEN001
Assignment 6"""

names =[]

# User is prompted to enter a list of names
name = input ("Enter strings (end with DONE):\n")
while name != 'DONE':
    names.append(name) # This appends/adds the name(s) the user types in, to names
    name = input("")


if names ==  []:
    print("\n""Right-aligned list:")
    for name in names:  
        maximum = max(names, key=len) 
        new_maximum = len(maximum) 
        diff = new_maximum - len(name)
        title = diff*' '
        print(title,name)
        break
      
else:
    print("\n""Right-aligned list:")
    max_length = max(len(name) for name in names)
    for name in names:
        print ('{0:>{1}}'.format(name, max_length))
        
