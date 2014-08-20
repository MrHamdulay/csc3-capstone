"""Assignment 8  Question 1
Yaseen Sulliman
5 May 2014"""


def is_palindrome(string): 
    """determine if the string is a palindrome"""
    if len(string)==2:
        if string[0]==string[1]:
            return True
    if len(string)==1:
        return True
    new_sentence=string[1:-1]
    if string[0]!=string[-1]:
        return False                
    elif string[0]==string[-1]:
        return is_palindrome(new_sentence)

def main():
    """function to incorporate palindrome fn"""
    sentence=input("Enter a string:\n")     
    bool_value=is_palindrome(sentence)
    if bool_value:
        print("Palindrome!")
    elif not bool_value:
        print("Not a palindrome!")
        
if __name__=="__main__":

    main()