#sheldon kisten
#8 may 2014
#is phrase palindrome?

word=input("Enter a string:\n")
def isPalindrome(word):
#test for base case    
    if len(word)== 1 or len(word)==0: #if word only has one letter it is already a palindrome
        print("Palindrome!")
    else:
        if word[0]==word[-1]:
            isPalindrome(word[1:-1])#testing "second layer"
        else:
            print("Not a palindrome!")  #when word is not palindrome
isPalindrome(word)            

