def reverse(wrd):
    if wrd == "":
        return wrd
    else:
        return reverse(wrd[1:]) + wrd[0]
    
string = input("Enter a string:\n")
if reverse(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
        
    
    
