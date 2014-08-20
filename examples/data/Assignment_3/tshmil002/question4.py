initial=eval(input("Enter the starting point N:\n"))
Final=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(initial+1,Final,1):
    n=str(i)
    m=" "
    for j in n[len(n)-1::-1]:
        m+=j
    if (int(n)==int(m)):
        prime="true"
        for k in range(2,int(n),1):
            if(int(n)%k==0):
                prime="false"
        if prime=="true":
            print(n)
                
        
    
    