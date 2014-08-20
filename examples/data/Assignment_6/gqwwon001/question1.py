# A programme that prints out the names in a list right aligned
# Wongwa Giqwa
# 20 April 2014

# Create an empty list
strings = []



# Get the list of strings 
string = input('Enter strings (end with DONE):\n')
x=0 #set max value to 0

while string != 'DONE':
    strings.append(string)
    length = len(string)
    string = input('')
    if length > x: # find string with max length
        x=length


print('\nRight-aligned list:')

for string in strings:
    print(string.rjust(x)) # right justify strings to max string length
        
    

    
    
    
    
        