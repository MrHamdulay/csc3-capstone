# Finding if palindrome using recursion    
# Brandon Hall (HLLBRA005)
# 09/05/2014
def palin(word):
    if (len(word) < 2):
        return("Palindrome!")
    elif(word[0] == word[-1]):
        return(palin(word[1:(len(word)-1)]))
    else:
        return("Not a palindrome!")
    
    

print("Enter a string:")  
word =  input()
print(palin(word))    