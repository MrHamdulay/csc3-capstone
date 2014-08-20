'''Luke Joseph
2014-05-07
question 1 of assignment 8'''

# Function calculating whether a palindrome or not
def palindrome(x):
    if x=="":
        return True
    else:
        if x[0]==x[len(x)-1]:
            return palindrome(x[1:len(x)-1])
        else:
            return False

# Main function printing outputs
def main():
    x=input("Enter a string:\n")
    y=palindrome(x)
    if y == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
main()