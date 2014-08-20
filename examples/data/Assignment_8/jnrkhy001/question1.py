#Khyati Jinerdeb
#Assignment 8
#Date Submitted:09/05/2014
#program to calculate whether a string is a palindrome or not

word=input("Enter a string:\n")
word=str(word)
#test for base case    
if len(word)== 1 or len(word)==0: #if word only has one letter then it is already a palindrome
    print("")
else:
        if word[0]==word[-1]:
            print("Palindrome!")
        else:
            print("Not a palindrome!")  #if word is not a palindrome
