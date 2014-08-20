#Assignment 8.1
#Michael Gant
#05/05/2014

def Palin(sText):
    if len(sText) < 2:
        return True
    if sText[0] == sText[-1] :
        return Palin(sText[1:-1])
    return False

sInput = input("Enter a string:\n")
if Palin(sInput):
    print("Palindrome!")
else:
    print("Not a palindrome!")
