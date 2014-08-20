#Thiolan Prevan Naidoo
#NDXTHI031
#question1  
#Check for palindromic string using recursion


word=input("Enter a string:\n")

def pal(word):
    if word == '':
        return True
    else:
        if word[0] == word[len(word)-1]:# checks if the first character in the string is the same as the same as the last character
            return pal(word[1:len(word)-1])#sends the word recieved by the pal function  without the first and last character back into the pal function
        else:
            return False
        
        
if pal(word)==True:
    print("Palindrome!")
else:
    print("Not a palindrome!")