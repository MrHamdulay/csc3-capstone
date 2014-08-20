# program where the user enters a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.
# Mulisa Badugela
# 20 April 2014


def main():
    names= [] # Empty list
    name=input('Enter strings (end with DONE):\n') # first user input 
    
    while name!='DONE':
        names.append(name)
        name=input()
    # the above part makes user continue to add names to the list until the user inputs 'DONE'
   
    print('\nRight-aligned list:')
    for i in names:
        longest=max(names,key=len) # helps us find the longest input
        len_longest=len(longest) # helps us find the legnth of the longest input
        len_names=len(i) # finds the legnth of each input
        length=len_longest-len_names
        print(length*' '+i)
        
main()