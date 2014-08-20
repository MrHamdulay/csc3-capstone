
#Dhriven Hamlall

def palindrome(string):
       
       if len(string) == 0 or len(string) == 1: 
              return "Palindrome!"
       elif string[0] != string[len(string)-1]:
              return "Not a palindrome!"
       else: 
              return palindrome(string[1:len(string)-1])
       
x= input("Enter a string:\n")
palindrome(x)
print(palindrome(x))