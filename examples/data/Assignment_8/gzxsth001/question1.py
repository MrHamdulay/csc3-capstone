""" a progamme to decide whether a string is a palindrome or not
Sthabiso Andile Gazu
May 2014"""
#ask the user for a string
string=input("Enter a string:\n")
def palindrome(string):
    if len(string)<=1:
        print("Palindrome!")
        return 
    elif len(string)>1:
        if string[0]==string[-1]:
            k=string[1:-1]
            return palindrome (k)
        else:
            print("Not a palindrome!")
            return


#to return whether it is a palindrome or not    

palindrome(string)

