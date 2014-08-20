# Author : Rayaan Fakier FKRRAY001
# Date : 20 - 04 - 2014
# question1.py
''' Program which compares set of strings and returns the list
right-aligned'''

def main():
    strngs = input("Enter strings (end with DONE):\n")
    strngs_list = [strngs]
    
    # Adds strings to a list (until sentinel is given)
    while strngs != "DONE": 
        strngs = input()
        strngs_list.append(strngs)
    strngs_list.remove("DONE") # Removes string entry 'DONE'
    
    # Sets longest str to maxlenstr
    maxlenstr = ""
    for i in strngs_list:
        if len(i) > len(maxlenstr):
            maxlenstr = i 
            
    print("\nRight-aligned list:")
    x = len(maxlenstr)
    for j in strngs_list:
        # Uses spaces to align strings relative to longest len(str)
        print(" " * (x - len(j)) + str(j)) 

main()