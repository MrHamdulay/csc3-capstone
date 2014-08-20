''' This programm prints strings right aligned
Nxumalo Goodman
20 April 2014'''

def right_aligned():
    strings = []
    string = input("Enter strings (end with DONE):\n")
    length = len(string)
    while string != "DONE":
        strings.append (string)
        string = input("")
        if length > len(string):
            length = length
        else:
            length = len(string)
    print()
    print("Right-aligned list:")
    for string in strings:
        print(" "*(length-(len(string)))+string)
          
right_aligned()