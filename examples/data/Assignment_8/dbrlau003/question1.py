#Lauren de Bruyn
#Palindrome recursion
#5 May 2014

palindrome= input("Enter a string: \n")

def palindrome_check(palindrome):
        if len(palindrome)==0 or len(palindrome)==1:
                print("Palindrome!")
        else:
                if palindrome[0] == palindrome[-1]:
                    return palindrome_check(palindrome[1:-1])
                else:
                    print("Not a palindrome!")

palindrome_check(palindrome)

