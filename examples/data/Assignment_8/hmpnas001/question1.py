"""program to check if a string is a palindrome
nasonkwe hampwaye 
2014-05-08"""

message=input("Enter a string:\n")
#palindrome=True
def pali(string):
        palindrome=True
        if len(string)<=1:
                palindrome=True 
        else:       
                if string[0]==string[-1]:
                        return pali(string[1:-1])
                else:
                        palindrome=False
        if palindrome:
                print("Palindrome!")
        else:
                print("Not a palindrome!")
               
pali(message)
    