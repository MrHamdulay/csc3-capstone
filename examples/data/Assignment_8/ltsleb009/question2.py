"""Counts number of paired occurances in a string"""

string = input("Enter a message:\n")

def pairs(string):
    """counts number of pairs in a given string"""
    if not string:
        return
    elif len(string) > 1 :
        # check the letters next to each other if they match and if they do add one
        if string[0] == string[1]:
            return 1 + pairs(string[2:]) #recursive step
        else:
            return 0 + pairs(string[1:]) #recursive step
    else:
        return(0)    

if not string == "":
    print("Number of pairs: {0}".format(pairs(string)))