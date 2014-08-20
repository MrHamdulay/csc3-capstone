
x = input("Enter a string:\n")
def Palindrome(x):
    if x[0] == x[-1]:
        if 1 == len(x) or 0 == len(x) or 2 == len(x):
            print("Palindrome!")
            return
        else:
            length=len(x)-1
            y = 1
            step = x[y:length]
            #print(step)
            Palindrome(step)
            #print("Palindrome!")
            return
    else:
        print("Not a palindrome!")
Palindrome(x)