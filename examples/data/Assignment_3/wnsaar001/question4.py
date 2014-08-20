start= eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1, end-1):
    c = True
    for j in range(2,i):
        if (i%j)==0:
            c =False
    if c== True:
        wordi = str(i)
        backw = wordi[::-1]
        if wordi==backw:
             print (i)
           
