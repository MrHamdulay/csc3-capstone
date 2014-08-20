""""Assignment 8
Question 1
Micaela Menegaldo"""

def palindrome_check(string):
    if string=="":
        print("Palindrome!")
    elif string[0]==string[len(string)-1]:
        palindrome_check(string[1:len(string)-1])
    else:
        print("Not a palindrome!")


if __name__=='__main__':
    sentence=input("Enter a string:\n")
    palindrome_check(sentence)