def palindrome(value):
    
    if value == "":
        return True 
        
    elif value[0:1] == value[-1:]:
        return palindrome(value[1:-1])
    
    else:
        return False


if __name__ == "__main__": # This allows program to be later imported into question 4   
    
    value = input("Enter a string:\n")
    
    if palindrome(value):
        print("Palindrome!")  
    
    else:
        print("Not a palindrome!")