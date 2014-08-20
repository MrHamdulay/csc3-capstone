
def palindrome(starting, finishing):
    for j in range(starting+1,finishing):
        if str(j) == str(j)[::-1]:
            if j == 2: print(j)
            for i in range(2,j):
                rem = j%i
                if rem ==0: break
                if i == j-1: print(j)
            
input1 = eval(input("Enter the starting point N:\n"))
input2 = eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
palindrome(input1,input2)