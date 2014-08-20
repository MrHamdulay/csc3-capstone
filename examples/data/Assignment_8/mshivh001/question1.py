#MAISHA IVHA
#Creating a programme that determines if a string is a palindrome or not
#09 may 2014

#def main():
word=input("Enter a string:\n")

def palindrome(word):
    #import main    
    #base case
    if word=="" or len(word)==1: #if the string is empty or the length of the string is 1, thestring  is palindrome, function should return.
        print("Palindrome!")
        return
    else:
        
        
        last_=word[-1] #obtaining the last character from the string
        
        if word[0]==last_: #
            
            word=word[1:-1] #recursive step that keeps on cutting down characters in a string
          
            if palindrome(word):
                print("Palindrome!")          
        else:
            print("Not a palindrome!")
palindrome(word)