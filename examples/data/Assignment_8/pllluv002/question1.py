#Palindrome checkr using recursion
#5/4/5014
#Author: Luveshen Pillay

# String processing to input function
word=str(input("Enter a string:\n"))
          

# main function
def palindrome(word):
    
    
    if len(word) == 0:
        print ("Palindrome!")
        
    elif word[0] != word[-1]:
            print ("Not a palindrome!")    
    
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
   
    elif len(word) == 1 :
        print (str("Palindrome!"))
    


palindrome(word)
    
