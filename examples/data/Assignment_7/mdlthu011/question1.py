#-------------------------------------------------------------------------------
# A program that create a list entered by the user, followed by the sentinel 
# DONE to indicate the user has finished entering the data. The repeated object 
# are removed from the list and the new list is printed without repeated items.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011
#-------------------------------------------------------------------------------

def main():
    print("Enter strings (end with DONE):")
    
    # Create an empty list and add the values entered by the user in the list.
    names = []          
    x = ""
    while x != "DONE":
        x = input()
        if x != "DONE":
            names.append(x)
    
    # Remove all the repeated items in the list. 
    newlist = []   
    for i in names:
        if i not in newlist:
            newlist.append(i) 
        
    # Display the new list.
    print()
    print("Unique list:")
    for j in newlist:
        print(j)

# Call the main function.
main()
    
