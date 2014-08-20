"""Program that check whether a sentence is palindromic
Aubrey Baloi
05 May 2014"""

def palindr(string = input("Enter a string: \n")):
    #string = input("Enter a string: \n")
    if string =='':
        return True
    if len(string) == 1:
        return True
    else:
        if string[0] == string[len(string)-1]:
            string = string[1:-1]
            if palindr(string):
                print("Palindrome!")
        else:
            print("Not a palindrome!")


palindr()