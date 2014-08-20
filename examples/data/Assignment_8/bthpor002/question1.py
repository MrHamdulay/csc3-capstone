#Determining whether something is a palindrome or not using recursion 

def palindrone(phrase):
    if len(phrase)%2!=0:
        if len(phrase) == 1:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrone(phrase[1:len(phrase)-1])
        else:
            return False
    else:
        if len(phrase) == 0:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrone(phrase[1:len(phrase)-1])
        else:
            return False        
    
#Get the phrasee that will be checked if it is a palindrom or not 
phrase = input("Enter a string:\n")

y=palindrone(phrase)

#Print out whther the phrase is a palindrome of not 
if y:
    print("Palindrome!")
else:
    print("Not a palindrome!")