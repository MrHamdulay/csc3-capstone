#Program to find palindromic strings
#Ethan Jackson
#9 May 2014

word = input("Enter a string:\n")
def palin(word):
    if word == '':
        return ("Palindrome!")
    else:
        if (ord(word[0]) - ord(word[len(word)-1])) == 0:#runs through string checking if first character is equal to the last
            return palin(word[1:len(word)-1])
        else:
            return ("Not a palindrome!")#if characters are not the same, then it is not a palindrome
print(palin(word))

            
            
        
        
    
