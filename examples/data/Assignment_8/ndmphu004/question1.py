#Phumelele Ndimande
#Assignment 8

def palindrome(string):
#Functionchecks if string is a palindrome
    if string[:1] == string[-1:]:
        if string == "":
            return "Palindrome!"
        else:
            return palindrome(string[1:-1]) 
    else:
        return "Not a palindrome!"
     
def main():
    string = input("Enter a string:\n")
    print(palindrome(string))
    

main()
