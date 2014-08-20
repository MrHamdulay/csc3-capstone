#-------------------------------------------------------------------------------
# A program that create a list entered by the user, followed by the sentinel 
# DONE to indicate the user has finished entering the data. The lists of objects
# entered by the user are printed out right-aligned.
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
    
    previous = ""        
    for i in names:
        if len(i) >= len(previous):
            x = len(i)
    
    # Display names.
    print()
    print("Right-aligned list:")
    for name in names:
        print(name.rjust(x))
        
# Call the main function.
main()
        