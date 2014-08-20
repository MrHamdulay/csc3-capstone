# Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
# Mulisa Badugela
# 30 April 2014

def main():
    old_list=[] # LIST FOR USER INPUTS
    uq_list=[] # LIST TO BE USED FOR UNDUPLICATED
    words=input('Enter strings (end with DONE):\n') # user input stirngs
    old_list.append(words) # add the string to the list 
    while words != 'DONE':
        words=input() # continue add until "DONE" 
        old_list.append(words)
    
    done=len(old_list)
    del old_list[done-1] # DELETE 'DONE' FROM THE STRING
    print('\nUnique list:')
    for i in old_list:
        if i not in uq_list:
            uq_list.append(i) # ADD ITEMS FROM THE FIRST LIST BUT NOT DUPLICATING THEM
    
    for i in uq_list:
        print(i) # PRINT OUT UNDUPLICATED LIST
main()
    