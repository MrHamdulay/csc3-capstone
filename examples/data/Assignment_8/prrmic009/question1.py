"""Program to check if input string is a palindrome or not
Mick Perring
07 May 2014"""

def palin(string):   # palin function (main function)
    if len(string) == 1:   # if function gets this far, string is a palindrome, so prints "Palindrome!"
        print("Palindrome!")
    
    elif len(string) == 2:           # if function gets this far, checks if middle two characters are 
        if string[0] == string[1]:   # the same and if so prints "Palindrome!"
            print("Palindrome!")
    
    if len(string) > 2:   # if string is longer than two characters, continues function
        if string[0] == string[-1]:   # if each end value is the same, removes them and repeats function
            return palin(string[1:-1])
        elif string[0] != string[-1]:  # if each end value not the same, not palindrome, prints "Not a palindrome!"
            print("Not a palindrome!")

        
string = str(input("Enter a string:\n"))
palin(string)