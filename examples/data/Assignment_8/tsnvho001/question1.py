"""Program to calculate whether or not a string is a palindrome
Tsanwani Vhonani
05 May 2014"""

#Get string from the user
word=input('Enter a string:\n')
def palindromic_strings(word):
   
    #if length of string is less than 2,the string is a palindrome
    if len(word)<2 :
        print("Palindrome!")
        return
   
    #if the length of the string is 2 and more check if the first letter and the last letter are the same
    elif len(word)>1:
        #If the last letter and first letter are not equal,it is not a palindrome
        if word[0]==word[-1]:
            new_word=word[1:-1]
            return palindromic_strings (new_word)
        
        #if last and first letter are the same,remove first and last letter of word until the last letters,checking if they are the same
        else:
            print("Not a palindrome!")
            return
        
palindromic_strings(word)

        

