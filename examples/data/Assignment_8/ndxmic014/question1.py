#NDXMIC014
#8 MAY 2014
#ASSIGNMENT 8
#QUESTION ONE

wrd=input("Enter a string:\n")

def check(wrd):#Creates a function called wrd
    if wrd == '':
        return True#if wrd is an emoty string it returns true
    else:
        if (ord(wrd[0]) == ord(wrd[len(wrd)-1])):
           
            return check(wrd[1:len(wrd)-1])
        else:
            return False#returns false
if(check(wrd)==True):
    print("Palindrome!")#if it is a palindrome then this is printed out 
else:
    print("Not a palindrome!")#if it is not a palindrome this is printed out