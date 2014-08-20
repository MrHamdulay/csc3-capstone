"""Program to print a list of supplied names right-aligned with the longest name.
Kemeshan Naicker
23 April 2014"""

def right_align():
    
    #Prompt user for list of names
    print("Enter strings (end with DONE):")
    #Create accumulator variable "strings" to store names.
    strings = []
    #Append names from user to the accumulator.
    next_name = input()
    while next_name != "DONE":
        strings.append(next_name)
        next_name=input()
    #Determine the longest name.
    lname=0
    for x in strings:
        if len(x)>=lname:
            lname=len(x)
    #Create new accumulator to store list of right-adjusted names.
    new_strings=[]
    #Loop through strings and use spaces to equate the length of every item to the length of the longest item.
    #Store "space-padded" item in the new list.
    for y in strings:
        while len(y)<lname:
            y=" "+y
        if len(y)==lname:
            new_strings.append(y)
    #Print the new list.
    print("\nRight-aligned list:")
    for z in new_strings:
        print(z)

if __name__=="__main__":
    right_align()