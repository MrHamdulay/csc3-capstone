"""thrianka naidoo
ndxthr005
assignment8: question 1"""

string = input("Enter a string:\n") #input for user

def Palindromes(string):                    #mehod
    if string =="":                         #stopping condition1
        return ""
    elif string==" ":                       #stopping condition2
        return " "
    else:
        return string[-1] + Palindromes(string[0:len(string)-1])

new_string = Palindromes(string)

if new_string == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")