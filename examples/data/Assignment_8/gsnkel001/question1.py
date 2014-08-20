#Palidrom function using recursion
#2014/05/09
#by Kelly Goosen



    
def palindrome (y):
    if len(y)<2:
        return True #is a plaindrom
    elif y[0]==y[-1]:return palindrome(y[1:-1])
    else: return False #not a palindrome
    
                    
def string():
    m=input("Enter a string:\n")
    if palindrome(m)==True: print("Palindrome!") #printing output if it is a palindrome
    else: print("Not a palindrome!") #printing output if it is NOT a palindrome
string()


