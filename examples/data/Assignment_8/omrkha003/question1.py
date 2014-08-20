# program with a recursive function to determine if a string is a palindrome
# khadeejah omar
# 4 May 2014


def palindrome(string) :

    # base case
    if string == "" or len(string) == 1:
        return ("Palindrome!")
        
    # recursive step
    else:
        if string[0] == string[-1] :
            return palindrome(string[1:-1]) # if the first letter and last letter of string is the same, slice those letters off and do recursive step again
        else :
            return ("Not a palindrome!") # if the first letter and last letter of the string is not the same


def main() :
    
    string = input("Enter a string: \n")
    print(palindrome(string))

main()