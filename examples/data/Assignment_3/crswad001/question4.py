start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
x=2
t1='t'
print("The palindromic primes are:")
for i in range(start+1,end):
    if str(i)[::-1]==str(i):
        while x<i:
            if i%x==0:
                t1='f'
            x+=1
        if t1=='t':
            print(i)
        x=2
        t1='t'            
    

