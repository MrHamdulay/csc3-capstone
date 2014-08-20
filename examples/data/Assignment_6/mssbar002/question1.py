"""Program to enter list of strings and print them right aligned with the 
longest string
Author: Barnett Msiska
Date: 23/04/2014"""

def main():
    #collect strings
    strings = []
    string = input("Enter strings (end with DONE):\n")
    while string != 'DONE':
        strings.append(string)
        string = input("")
    #find longest string
    longest = 0
    for n in strings:
        if len(n) > longest:
            longest = len(n)
    #print out strings
    print("\nRight-aligned list:")
    for n in strings:
        print(" "*(longest - len(n)) + n)
        
main()
        