#Saijil Nemchund
#NMCSAI001
#Question 1 

word=input("Enter a string:\n") #Asking the user for an input 

def check(word):
    if word == '': #Checking if the output is empty
        return True
    else:
        if (ord(word[0]) == ord(word[len(word)-1])): #Checking if the letters in the word are a mirror image of each other 
            
            return check(word[1:len(word)-1])
        else:
            return False
if(check(word)==True): #If the word has identical letters on both halves of the word, it is a palidrome. 
    print("Palindrome!")
else:
    print("Not a palindrome!") #If the word doesn't have identical letters on both halves of the word, it is not a palidrome.