#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 1


def inverse(string): #function to reverse the input
    if string=="":
        return string #empty string
    else:
        return (inverse(string[1:])+string[0]) #using recursion to keep putting the first letter to the end of the word, returns the original word completely reversed
    
word = input("Enter a string:\n")
if word==inverse(word): #if it is a palindrome
    print("Palindrome!")
else:
    print("Not a palindrome!")