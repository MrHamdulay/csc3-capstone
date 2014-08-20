'''Q1 of Assignment 8: Testing if a string is a palindrome
Patrick Boroughs
4 May 2014'''

def palindrome(string):
    
    #reached middle of word and still palindrome
    if len(string)<=1:
        return True
    
    #test if characters on either end match and return smaller string
    elif string[0]==string[-1]:
        return palindrome(string[1:-1])
    
    #characters on end don't equal before reaching middle
    else:
        return False

#input and print 
if __name__ == "__main__":
    ans = palindrome(input("Enter a string:\n"))
    if ans:
        print("Palindrome!")
    else:
        print("Not a palindrome!")