#Kovlin Perumal
#PRMKOV001
#09/05/2014
#Recursive Palindrome Function

inputWord = input("Enter a string:\n") #Recieve input
 

def palinCheck(word) :#Define function to check whether palinrome
   
    if len(word) == 1 or len(word) == 0:
        return True #If the length of the word is 1 it has to be the same backwards and forwards if its 0 the recursion has been exhausted
    else :
        if word[0] != word[-1] :
            return False #Account for non palindromes
        else:
            return palinCheck(word[1:len(word) - 1])#Cut out first letter of word and recall
        
if palinCheck(inputWord) == True :
    print("Palindrome!")
else :
    print("Not a palindrome!")
            
        
    
    
