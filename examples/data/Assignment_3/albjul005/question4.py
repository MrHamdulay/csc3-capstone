# Palandromic prime search in an inputed interval

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(start+1,end):
    a = True
    for v in range (2, i//2+1):
        if (i%v == 0):
            a = False
            break
    if a:
        i=str(i)
        if i!=i[::-1]:
            a = False
    if a:
        print(i)
        
