"""a program with a recursive function to calculate whether or not a string is a Palindrome
fadzai mupfunya
6 may 2014"""

string_space=input("Enter a string:\n")

def palindrome(string, index): 
    #first base case to check whether the letters are equal by checking the middle value of the string
    if int(len(string)//2) == index:
        print("Palindrome!")
        return
    
    #to check whether the first character and the last character are equal
    if string[index] != string[len(string)-1-index]: #subtract 1 to get index. Subtract index to get the next letter from the last character
        print("Not a palindrome!")
        return
    else:
        return palindrome(string, index+1) #to add the index by one each time function is called
    
palindrome(string_space,0) #use 0 to get the function started


