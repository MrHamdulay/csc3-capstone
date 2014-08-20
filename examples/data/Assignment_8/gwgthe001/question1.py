#Thembekani Gwegwana
# A program to determine whether a string is a palindrome or not
#May 2013


string = input('Enter a string:\n') #Ask the user for input

def palindrome(string):
    #Base case
    if len(string)<= 1 :
        return 'Palindrome!'
    # Recursive step
    else:
        if string[0] == string[len(string)-1]:   #Comparing the first character of the stringg to the last
            return palindrome(string[1:len(string)-1])
        else :
            return "Not a palindrome!"
print(palindrome(string))