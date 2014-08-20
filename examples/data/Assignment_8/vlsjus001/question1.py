#question1
#author:justin valsecchi
#2014/05/08

#creating a base case
def reverse(p):
    if len(p) == 1: 
        return p
    else:
        return p[-1] + reverse(p[:-1])
#use of return funtion, istead of iteration loops
#continuing through the other parts
string = input("Enter a string:\n")
if reverse(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")