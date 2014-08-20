# A palindrome is a word, phrase, number, or other sequence of symbols or elements, whose meaning may be interpreted the same way in either forward or reverse direction 


def rev(p):
    
    if len(p) == 1:
        return p
    
    else:
        return p[-1] + rev(p[:-1])


string = input("Enter a string:\n")


if rev(string) == string:
    print("Palindrome!")
    
else:
    print("Not a palindrome!")
