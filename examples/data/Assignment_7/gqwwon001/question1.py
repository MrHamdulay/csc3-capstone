# A program to print out strings in sequence
# Wongwa Giqwa
# 27 April 2014


strings = [] # create an empty string

string=input('Enter strings (end with DONE):\n') # Get user to type in name


while string != 'DONE': 
    strings.append(string)
    string =input ('')
counter = [] 
    
for string in strings:
    if not string in counter:
        counter.append(string)
    else:
        continue
    
print('\nUnique list:')        
for string in counter:
    
    print(string)
    

    
    


