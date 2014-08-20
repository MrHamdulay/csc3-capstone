# question1.py
# a program where the user can enter a list of strings and theses strings 
# are then printed in the same order but without duplicates
# Thomas Konigkramer
# 27 April 2014

def no_duplicates():
    
    # introductory statement: not already input, in case first word = done
    print("Enter strings (end with DONE):")
    
    # creating empty list and string to be used in loop
    # looping through string
    # if DONE, break
    # appending all other never-before seen strings to list
    string = ""
    string_list = []
    while string != "DONE":
        string = input()
        if string == "DONE":
            break
        elif string not in string_list:
            string_list.append(string)
            
    print()
    # printing output
    print("Unique list:")
    for string2 in string_list:
        print(string2)

no_duplicates()
        