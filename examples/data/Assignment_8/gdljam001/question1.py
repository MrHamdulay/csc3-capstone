"""James Godlonton
check if palindrome using recursion
04 May 2014"""

def main():
    """Main function for input output and to call check function"""
    print("Enter a string:")
    word=input("")
    if checkPalin(word,0):
        #Calling check function to see if palindrom
        print("Palindrome!")
    else:
        print ("Not a palindrome!")
    
def checkPalin(wordCheck, letter):
    """recursive function that checks the letters "letter" away from the beggining and end to see if they equal"""
    if letter==len(wordCheck)-1-letter:
        #if you reach middle of string (odd) without falt the must be palindrom
        return True
    elif letter-1==len(wordCheck)-1-letter:
        #if you reach middle of string (even) without falt the must be palindrom
        return True
    elif wordCheck[letter]!=wordCheck[len(wordCheck)-1-letter]:
        #if two letters do not match then return false and end recursion
        return False
    else:
         #checks to see if the next 2 letters will pass the test (recursice step)
        return checkPalin(wordCheck, letter+1)
   
    
if __name__== "__main__":
    main()

    
    
    
    
    
    