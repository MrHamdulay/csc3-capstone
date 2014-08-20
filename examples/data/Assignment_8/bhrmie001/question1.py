# Miengha Behardien
# Assignment 8
# 4 May 2014

def palindrome(sentence):           #checks if sentence is a palindrome
    if len(sentence)==2:
        if sentence[0]==sentence[1]:
            return True
    if len(sentence)==1:
        return True
    new_sentence=sentence[1:-1]
    if sentence[0]!=sentence[-1]:
        return False                #returns false if not palindromic
    elif sentence[0]==sentence[-1]:
        return palindrome(new_sentence)

def main():
    sentence=input("Enter a string:\n")     #runs all the bells and whistles
    bool_value=palindrome(sentence)
    if bool_value:
        print("Palindrome!")
    elif not bool_value:
        print("Not a palindrome!")
        
if __name__=="__main__":

    main()