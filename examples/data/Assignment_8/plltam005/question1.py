""" finding palindrome using recursion
Tamery Pillay
9 May 2014 """

# string input
x = input("Enter a string:\n")
y = len(x)-1

def palin (y):
       
    if y == 0:
        return x[0]   # base case
    else:
        return x[y] + palin(y-1)   # recursive step
    
p = palin(y) # make function equal to variable 

# check to see if palindrome or not
def main():
    if x == p:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
main()
    