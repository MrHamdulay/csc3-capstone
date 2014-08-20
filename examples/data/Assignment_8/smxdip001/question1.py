#Program to check palindrome
#Dipanjali Samoo
#SMXDIP001
#11.05.2014

def check_pal(string):
    if len(string)<2:
        return print("Palindrome!")
    
    else:
        if (string)[0]==string[-1]:
            return check_pal(string[1:-1])
        
        #if the string entered is not a palindrome
        else:
            return print("Not a palindrome!")
        
string=input("Enter a string:\n")
check_pal(string)