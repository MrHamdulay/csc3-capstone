"""program with a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed). 
leandra govender
05 May 2014"""



#function to reverse the string
def reverse(word):
    if len(word) == 0 or len(word) == 1:        # if the string is one letter or the string is zero return the entered string
        return(word)
    else:
        return word[len(word) - 1] + reverse(word[1:len(word) - 1]) + word[0]         #use recursion to rverse the string
    
# input string from user
def palin():
    word = input("Enter a string:\n")
    
    # compare input string to reversed string
    if reverse(word) == word:                          #if the reversed word is equal to the entered word it is a palindrome
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        

palin()