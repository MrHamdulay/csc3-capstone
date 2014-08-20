#Recursive program to check if a string is a palindrome
#Tyrone Arnold
# 9 April 2014

def palindrome(s):
   
    if s == "": #empty string is a palindrome
        result = True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:  #if the position of string index at pos1 = string index at pos2
            return palindrome(s[1:len(s)-1])    #recurse through  the next position in the string
        else: #not equal therefore not palindrome
            result = False
    return result


s = input("Enter a string:\n") #allows input outside recursive function
palindrome(s)

if palindrome(s) == True: #if result is true
    print("Palindrome!")
else: #if result is false
    print("Not a palindrome!")