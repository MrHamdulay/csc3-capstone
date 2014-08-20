"""This function counts the number of pairs of letters in a massage
Masilela Mduduzi
07 may 2014"""
string = input("Enter a message:\n")
def count(string):
    if len(string)<=1:#checks if the lenght of string is less than 1 or not
        return 0
    elif string[0]==string[1]:
        return 1 + count(string[2:])
    else :
        return count(string[1:])
print("Number of pairs:",count(string))