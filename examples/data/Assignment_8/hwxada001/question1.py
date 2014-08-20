word = input("Enter a string:\n")
def check_Palindrome(word):
    
    
    if len(word) ==1 or len(word) ==0:
        return True
        
    elif(word[0] == word[-1]):
        return check_Palindrome(word[1:len(word)-1])
    else:
        return False
    
if check_Palindrome(word) == True:
    print("Palindrome!")
else:
    print("Not a palindrome!")
        