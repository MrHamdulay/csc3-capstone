#ASSIGNMENT 8
#QUESTION 1
#NLTWES001

teststring=input("Enter a string:\n")

def reverse(teststring):
    if teststring=="":
        return teststring
    else:
        return reverse(teststring[1:]) + teststring[0]

if teststring==reverse(teststring):
    print("Palindrome!")
else:
    print("Not a palindrome!")