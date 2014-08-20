# Program to print a list of strings right-justified
# Dalise Steynfaard
# STYDAL001
# 26 April 2014

def rightJust(names):
    """Prints a list of names right-justified"""
    longest_name = 0
    
    for i in names:
        if len(i) > longest_name:
            longest_name = len(i)
            
    print('\nRight-aligned list:')
    
    for j in names:
        print(j.rjust(longest_name))

def main():
    """Gets a list of names from the user"""
    names = []
    current_name = input('Enter strings (end with DONE):\n')
    
    # Adds names to list names
    while current_name != 'DONE':
        # if the string is not empty
        if current_name:
            names.append(current_name)
        current_name = input('')
    
    rightJust(names)

main()