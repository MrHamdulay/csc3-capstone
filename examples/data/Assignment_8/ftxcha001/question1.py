#Chantel Foot
#Question 1
#Assignment 8

def palin(word):
    
    if len(word) < 2: #if user puts in a single letter then will return as true. 
        #not equal to 2 cause not neccessarily a palindrome 
        return True
    
    elif word[0] == word[-1]: #first letter equals last letter 
        return palin(word[1:-1]) #cut the first and last and then iterate again

    else: #if does not meet requirements of the above 2 then returns as false
        return False 
    
    
def string():
    x = input("Enter a string:\n")
    if palin(x) == True: # if word is a palindrome then print ...
        print("Palindrome!")
    else: # if word false, then print ...
        print("Not a palindrome!")
        
string() #call string function 
