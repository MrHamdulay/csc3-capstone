number = input("Enter the starting point N:\n") 
number2 = input("Enter the ending point M:\n")
print("The palindromic primes are:")
for i in range(eval(number)+1,eval(number2)): 
    f = len(str(i)) 
    number3 = str(i) 
    tnum = "" 
    for p in range (f): 
        tnum = tnum + number3[(f-1)-p]
    if str(i)== tnum:       
        print(i)