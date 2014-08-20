#Assignment 8, Question 1
#Avreyna Kistensamy
#3 May 2014
#check = input("Enter a string:\n")

def palin(check):
    if len(check) <1:
        print("Palindrome!")
    else:
        if check[0]==check[-1]:
            return palin(check[1:-1])
        else:
            print("Not a palindrome!")


x = input("Enter a string:\n")
check = x
palin(check)
    


