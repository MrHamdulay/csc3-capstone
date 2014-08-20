#PIET MOTALAOTA
#11 MAY 2014
def palindromes(word):
    if len(word) <= 1:
        return True
    elif word[0]==word[-1]:
        return palindromes(word[1:len(word)-1])
    else:
        return False
if __name__=='__main__':
    word =input("Enter a string:\n")
    if palindromes(word):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
                           