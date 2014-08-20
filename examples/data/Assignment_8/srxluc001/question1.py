def word(x):
    if x=="":
        return x
    else:
        return word(x[1:])+x[0]
def main():
    Q=input("Enter a string:\n")
    r=word(Q)
    if Q==r:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
main()