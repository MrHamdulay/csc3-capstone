# Program to right-align input strings
# Nomsa Gamedze
# 21 April 2014

def align_str():
    global strings
    global longest
    strings = ""
    print("Enter strings (end with DONE):")
    string = input("")
    while string != "DONE":
        strings += string + "sep"
        string = input("")
    longest = ""
    strings = strings.split("sep")
    for x in strings:
        if len(x) > len(longest):
            longest = x # Finds the longest string in the list
    y = len(longest)
    print('\n'"Right-aligned list:")
    for i in strings:
        print(i.rjust(y))
        
align_str()