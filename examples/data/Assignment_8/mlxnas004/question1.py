"""nasha somoina meoli
5th march 2014
program to check for palindromes"""

# get input from the user
string = input("Enter a string:\n")
string2= string
#reverse the string
def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]
    
string3 = reverse(string)
#check if the reversed value is equal to the previous one
if string3 == string2:
    print("Palindrome!")
else:
    print("Not a palindrome!")