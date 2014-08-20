#26 March 2014          #Mazwi Myeza
#Assignment3            #Question4

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palPrime = False
for i in range (start+1,end):
    j = str(i)
    k = j[::-1]
    palPrime = False
    for t in range(2,i):
        if i%t is not 0:
            if j == k:
                palPrime = True
            else:
                palPrime = False
                break
        else:
            palPrime = False
            break
    if i ==2:
        palPrime = True
    if palPrime == True:
        print(i)