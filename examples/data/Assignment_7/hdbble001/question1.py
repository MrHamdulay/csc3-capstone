"""print unique words from a given list
blessings hadebe
27 april 2014"""


def get_strings():
    """gets strings inputed by the user and adds them to a list"""
    strings=[]
    str=input("Enter strings (end with DONE):\n")
    while str!= 'DONE':
        strings.append(str)  #adds string inputed by the user to the array strings
        str=input()
    return strings


def unique_Strings():
    """creates an array of unique strings"""
    uniqueLst=[]
    for string in get_strings():
        if not string in uniqueLst:
            uniqueLst.append(string) #adds a new string not previously encountered to the array uniqueLst
    return uniqueLst

List=unique_Strings() 
print()
print("Unique list:")
for i in List:
    print(i) #iterates through the array List, and prints each string