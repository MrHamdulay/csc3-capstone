#Recursion
#MTHKHI001
#Question1
"""this is a program that uses recursion to test for palindromic strings"""



def test_palindrome(sentence,length,counter):
    
    if counter == length:
        return True
    
    else:
        #print(str(sentence[counter]))
        #print(str(sentence[counter- length]))        
        if sentence[counter] == sentence[-(counter+1)]:
            
            return test_palindrome(sentence,length,(counter+1))
        
        if sentence[counter] != sentence[-(counter+1)]:
            return False



sentence = input("Enter a string:\n")
length = len(sentence)
counter = 0

palindromic = test_palindrome(sentence,length,counter)

if palindromic == False:
    print("Not a palindrome!")
    
if palindromic == True:
    print("Palindrome!")
