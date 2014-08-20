# 8 May 2014
# Shaun Muzenda
# Program that uses a recursive function to count the number of pairs of repeated characters in a string

string = input("Enter a message:\n") #enter the messagee

def pairs(string):
    
    if string == "": #if no string inserted, returns 0
        return 0
    elif (len(string)==1):  #checks whether string length is equal to one
        return 0    #returns zero if string length is equal to 1
    
    else:
        if string[0] == string[1]:  #checs whether two succesive characters are the same
            string = string[2:]
            return 1 + pairs(string)
        else:
            return pairs(string[1:])
        
print_string = pairs(string)
print("Number of pairs: " + str(print_string))  #prints the number of pairs in the inouted string