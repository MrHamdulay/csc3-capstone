#Kiuran Naidoo
#Assignment 8
#Question 1
#5 May

def palindrome(word): #Check if word is palindrome
    if len(word) < 2: #Base Case. If length is less than two there must be a single letter or none at all
        return True
    elif word[0] == word[-1]: #Check first and last characters are equal
        return palindrome(word[1:-1]) #Call function with string that is truncated 1 character on either side
    else:
        return False
   

wordInput = input("Enter a string:\n")#Get Input

if palindrome(wordInput):#Print correct output 
    print("Palindrome!")
else:
    print("Not a palindrome!")

    


        
        
