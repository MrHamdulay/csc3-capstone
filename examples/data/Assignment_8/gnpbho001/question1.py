#gnpbho001
#actsci
word=input("Enter a string:\n")  
#if wrd nly has 1 letter then palidrome
word=str(word)
if len(word)== 1 or len(word)==0:
        print("")

else:
        if word[0]==word[-1]:
                
                print("Palindrome!")
        else:
                print("Not a palindrome!")
    #when word is not palindrome
