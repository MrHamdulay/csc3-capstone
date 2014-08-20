# a Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates
# Budeli Rendani
# BDLREN001
# 28/04/2014


import collections # Importing collection in order to arrange the words in the order they were entered
def main():
    z=[]
    x=input("Enter strings (end with DONE):\n") # Obtaining input from the user
    z.append(x) # Adding the input to the empty list
    while x != "DONE":
        x=input() # Obtaining input from the user
        z.append(x) # Adding the input to the empty list
    c=len(z) # Finding the number of strings in the  list in order to delete the word DONE from the list
    del z[c-1] # Deleting the word DONE from the list
    
    print("\nUnique list:")
    # Creating a count dictionery which counts the number of repitions of the words in a list and only prints out the words without the count
    counts={}
    counts=collections.OrderedDict(counts) # Arranging the words in the order they were entred.
    for i in z:
        counts[i]=counts.get(i,0) +1 
    y=list(counts.keys()) 
    
    for i in y:
        print(i) # Printing out the words without their count
main()