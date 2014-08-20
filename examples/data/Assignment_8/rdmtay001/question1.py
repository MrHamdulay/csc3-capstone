# 8 May 2014
# Tayla Radmore
# Program to find a palindrome



def palindrome(x):
    length=len(x)
    if x[0]==x[-1] or length==0 :        
        if length==1 or length==0:
            return "Palindrome!"
        elif length==2:
            if x[0]==x[-1]:
                return "Palindrome!"
            else:
                return "Not a palindrome!"
            
        else:
            return palindrome(x[1:length-1])
    else: 
        return "Not a palindrome!"

    
    
x=input("Enter a string:\n")    
print(palindrome(x))    

    