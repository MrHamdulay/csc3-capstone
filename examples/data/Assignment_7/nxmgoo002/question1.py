'''this program removes the duplicates from the list
Nxumalo Goodman
27 April 2014'''

def duplicate():
    strings = []
    string = input("Enter strings (end with DONE):\n")
    while string != "DONE":
        if string not in strings:
            strings.append(string)
        string = input("")
    
    #output of the list with no duplicates
    print()
    print("Unique list:")
    for i in strings:
        print(i)
        
duplicate()