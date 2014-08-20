#find odd integer palindromes in given range
#created by tafara mtutu
#23 march 2013
def palindrome(start, end):
    for j in range(start+1,end):
        if str(j) == str(j)[::-1]:
            if j == 2: print(j)
            for i in range(2,j):
                rem = j%i
                if rem ==0: break
                if i == j-1: print(j)
            
a = eval(input("Enter the starting point N:\n"))
b = eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
palindrome(a,b)