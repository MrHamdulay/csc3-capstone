#Program to find pairs of characters in a string
#By Megan Swartz
#12th May 2014

#checks for pairs within a string, returning 1 for every pair found
def pairs(string):
    if len(string)<=1:
        return 0
    if string[0]==string[1]:
        return 1+pairs(string[2:])
    else:
        return pairs(string[1:])

#Ask for input and return number of pairs
string=input("Enter a message:\n")
print("Number of pairs:",pairs(string))