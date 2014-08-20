starty= eval(input("Enter the starting point N:\n"))
endy = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(starty+1, endy-1):
    cc = True
    for j in range(2,i):
        if (i%j)==0:
            cc =False
    if cc== True:
        wordif = str(i)
        backward = wordif[::-1]
        if wordif==backward:
            print (i)