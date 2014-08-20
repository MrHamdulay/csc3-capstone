"""
Prashanth Sridharan
SRDPRA001
Assignment 4
boxes
"""

def print_square():
    print("*"*5)
    for p in range(0,3):
        print("*   *")
    print("*"*5)
    
def print_rectangle(wth, ht):
    print("*"*wth)
    for p in range(0,ht-2):
        print("*"+(" "*(wth-2))+"*")
    print("*"*wth)

def get_rectangle(wth, ht):
    string=("*"*wth)
    for p in range(0, ht-2):
        string+= "\n*"+(" "*(wth-2))+"*"
    string+="\n"+"*"*wth
    return string