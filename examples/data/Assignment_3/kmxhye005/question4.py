#question 4
           
start = eval (input("Enter the starting point N:\n"))
End = eval (input("Enter the ending point M:\n"))
print ("The palindromic primes are:")

for i in range (start+1,End):
    if (str(i) == str(i)[::-1]):
        c1 = i
        c2 = 0
        for j in range (c1):
            no = c1%(j + 1)
            if no == 0:
                c2 = c2 + 1
        if c2 == 2:
            print (c1)

