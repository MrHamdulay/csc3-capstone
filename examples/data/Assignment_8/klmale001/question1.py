"""Program to check for palindromes
Alexi Kalamoudacos
6 May 2014"""

#ask user for text

x = input("Enter a string:\n")

def is_pal(x):
    #If the strings length is 3 or shorter with the same starting and ending letteres,
    #then it is a palindrome.
    if x[0] == x[len(x)-1] and len(x) <= 3:
        print("Palindrome!")
    
    #if the beginning and ending letters are equal, with a length greater than 3, remove the first and last character and continue
    elif x[0] == x[len(x)-1]:
        return is_pal(x[1:len(x)-1])
    
    #if the starting and ending characters are different, there is no palindrome
    else:
        print("Not a palindrome!")
        
if __name__=="__main__":
    is_pal(x)
        