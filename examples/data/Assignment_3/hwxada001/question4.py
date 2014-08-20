s = input("Enter the starting point N:\n")
e = input("Enter the ending point M:\n")
print("The palindromic primes are:")
temp = ""
last = ""
k = True
if eval(s) <= 2:
    print("2")
for i in range(eval(s)+1,eval(e)):
    for j in range(2,i):
        temp = str(i)
        if(i%j==0):
            k=False
        if(temp == temp[::-1] and k == True and j==i-1):
            if(last != i):
                print(i)
                last = i
    k=True