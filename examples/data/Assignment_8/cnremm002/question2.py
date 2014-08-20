"""Count pairs of characters
Emmanuel Conradie
09 May 2014"""

#enter string
string = input("Enter a message:\n")

def pairs(string):
    
    #check if string length is > 2
    if string == "":
        return 0
    elif (len(string)==1):
        return 0
    
    #count pairs in string
    else:
        if string[0] == string[1]:
            string = string[2:]
            return 1 + pairs(string)
        else:
            return pairs(string[1:])

#print number of pairs   
print_string = pairs(string)
print("Number of pairs: " + str(print_string))