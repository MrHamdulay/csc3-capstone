#Konrad Hugo
#2014-05-06
#Assignment 8 question 1
#Recursion son!


word=input("Enter a string:\n")

    
def palindromePal(word): #function to determine whether string is palindrome or not
    
    
    if len(word) == 1 or len(word) == 0: #base case: whether odd length or even length, the palindrome will be recognised once this condition is met
        print("Palindrome!")
    else:
        if word[0] == word[-1]: # if last letter = first letter, move on ('loop' on)(recur on)
            return palindromePal(word[1:-1]) #makes recursion possible as the string returned excludes the first and last letter
        else: 
            print("Not a palindrome!") #if at any time, first letter != last letter, break out and declare the situation
        


palindromePal(word) #initiation propagation
        
    
    