start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
m = start
n = end

print ("The palindromic primes are:\n")
while m <= end:
    for i in range(start,end):
        ic = str(i) #convert the number to a string
        ir =  Si[::-1] #reverse the number
            
        if ic == ir :
            print(ic)
        i += 1