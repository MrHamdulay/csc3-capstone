"""a program that uses a recursive function to count the number of pairs of 
repeated characters in a string
Barnett Msiska
05/05/2014"""

def main():
    s = input("Enter a message:\n")
    pairs = countPairs(s)
    print("Number of pairs:", pairs)

def countPairs(s):
    """counts the number of paired characters"""
    if s == "" or len(s) == 1:
        return 0
    else:
        if s[0] == s[1]:
            return 1 + countPairs(s[2:])
        else:
            return countPairs(s[1:])
main()