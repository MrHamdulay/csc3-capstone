"""Assignment 8 - Q1
Zaheer Mahmood
5 - 05- 2014"""

#determine if plaindrome
def palindrome(string):          
    if len(string)==2:
        if string[0]==string[1]:
            return True
    if len(string)==1:
        return True
    new_sentence=string[1:-1]
    if string[0]!=string[-1]:
        return False                
    elif string[0]==string[-1]:
        return palindrome(new_sentence)

#create function to incorporate functions
def main():
    sentence=input("Enter a string:\n")     
    bool_value=palindrome(sentence)
    if bool_value:
        print("Palindrome!")
    elif not bool_value:
        print("Not a palindrome!")
        
if __name__=="__main__":

    main()