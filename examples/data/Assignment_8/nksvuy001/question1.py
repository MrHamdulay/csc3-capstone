"""program with a recursive function to calculate whether or not a string is a palindrome
vuyolwethu nkosi
4 may 2014"""

#program to identify palindromes
def palindrome(strng, one_char):
    #strng=input("Enter a string:\n")
    if len(strng)/2>=one_char: #if the string does not contain an empty space or just one letter, program can continue ie. Base Case
        if strng[one_char]==strng[-1-one_char] and palindrome(strng, one_char+1)== "Palindrome!": #step 1: checking to see whether the first character of the first word is the same as the last letter of the last word, then store this information and carry on # step 2:calling the function again but with new string defined ie.recursive step
            return "Palindrome!" #if conditions are met, it is a palindrome
        else: #if this is not the case, the input is not a palindrome
            return "Not a palindrome!"
    else:
        return "Palindrome!"
if __name__ == "__main__":  #calling the function
    strng=input("Enter a string:\n") #get input from user
    print(palindrome(strng,0)) #print 
