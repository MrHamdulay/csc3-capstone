def main():
    user_input = input("Enter a string:\n") 
    newStr = ""
    if len(user_input) > 0: #reverse string only if there are elements in it       
        newStr += check_palindrome(user_input)
        
    if newStr == user_input:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        

def check_palindrome(string):
    """recursive function that reverses a string"""
    if len(string) == 1:
        return string
    return string[-1] + check_palindrome(string[:-1])#reverse string
    

if __name__=="__main__":
    main()