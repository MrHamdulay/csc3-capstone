"""Assignment 8, Question 1
Tejasvin Bagirathi BGRTEJ001
program to check if string is palindrome"""

#Prompt user input
word = input('Enter a string:\n')


def palindrome(word):
   #If the first and last letter are the same and there are fewer than 3 letters in between them
   #then the word must be a palidrome
   if word[len(word)-1] == word[0] and len(word) <= 3:
      print('Palindrome!')
   
   #Remove the first and last letter if they are the same 
   elif word[0] == word[len(word)-1]:
      word = word[1:len(word)-1]
      return palindrome(word)
   
   #If the first and last letter are not the same, then it is not a palindrome
   else: print('Not a palindrome!')
 
palindrome(word)


   
      
   
      
   
      
   
      
      
    