"""Recursive Pair Counter"""
#Liam Brodie
#BRDLIA004
#May 2014

print("Enter a message:")
string = input("")
count = 0
global pairlist
pairlist = []

def paircount(string):
    """Counts the number of character pairs in a string"""
    if len(string) > 1:                 #Check if string is greater than 1 letter
        if string[0] == string[1]:      #Check if two adjacent letters are equal
            global count
            count += 1
            string = string[2:]
            return paircount(string)    
        elif string[0] != string[1]:    #Check if two adjacent letters are unequal
            string = string[1:]
            return paircount(string)
        
    if len(string) <= 1:                #Check if the string consits of 1 letter or none
        print("Number of pairs:", count)
    
paircount(string)