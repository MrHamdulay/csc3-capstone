#Gillian Wachira
#09 May 2014




def palindrome(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            # v-- forgot this here
            return palindrome(s[1:len(s)-1])
        else:
            return False       
def main():
    d=input("Enter a string:\n")
    
    
    if(palindrome(d) == True):
        
        print("Palindrome!")
    else:
        
        print("Not a palindrome!")
main()