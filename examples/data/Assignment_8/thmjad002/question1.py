"""Assignment 8, Question 1
JT
05-05-2014"""


def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    
def check(s1,s2):
    if s1 == s2:
        return True
    else:
        return False


def main():
    if __name__ == '__main__':
        string = input("Enter a string:\n")
        if check(string,reverse(string)):
            print("Palindrome!")
        else:
            print("Not a palindrome!")
        
main()