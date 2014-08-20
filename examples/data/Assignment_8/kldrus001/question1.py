#program with a recursive function 
#Rushil Kalidas
#7 May 2014


def reverse(word):
    if len(word) == 0 or len(word) == 1:        
        return(word)
    else:
        return word[len(word) - 1] + reverse(word[1:len(word) - 1]) + word[0]         
# input string from user
def palin():
    word = input("Enter a string:\n")
    
    # compare input string to reversed string
    if reverse(word) == word:                          
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        

palin()