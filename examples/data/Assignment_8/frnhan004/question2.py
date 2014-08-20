"""Question 2-Assignment 8
FRNHAN004
4 May 2014"""


string=input("Enter a message:\n")
def repeat_char(string):
    if len(string)<2: #if there arent two characters to look at return 0
        return 0
    else: #look at 2 characters
        if string[0]==string[1]: #if the first character and the second character are equal return 1 and then look at next set of characters
            return 1+repeat_char(string[2:]) 
        else: #if the first character and the second character arent equal return 0 and then look at rest of characters
            return 0+repeat_char(string[1:])

print("Number of pairs:",repeat_char(string), end="")
