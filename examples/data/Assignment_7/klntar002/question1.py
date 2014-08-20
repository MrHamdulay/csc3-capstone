# tarisai kalinde
# klntar002
# program to enter list of strings and return without duplicates

string_input=input('Enter strings (end with DONE):\n')
_array=[]                    # empty dictionary for the accumulation of strings

#while loop for the input continuation
while string_input!= 'DONE':
    
    if string_input not in _array: # ADDING INPUT TO THE ARRAY
        _array.append(string_input)
    
    string_input=input('')   

print('\nUnique list:')

# WHILE LOOP FOR PRINTING OUT THE REQUIRED OUTPUT    
for i in _array:
    print(i)
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

