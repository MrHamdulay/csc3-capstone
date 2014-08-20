start= eval(input("Enter the starting point N:\n"))

end= eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1, (end)):
    #print(i)
    prime="true"
    for j in range(1,i):
        #print(j)
        if (j!=1) and (j!=i):
            if(i%j==0):
                prime="false"
                break
    if(prime=="false"):
        continue
    if(i!=1) :
        ist= str(i)
        p= ist[::-1]
        # print(p)
        if(p==ist):
            print(ist)
