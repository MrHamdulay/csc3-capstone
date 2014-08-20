start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:",end="\n")
for i in range(start+1,end,1):
        n = str(i)
        m = ""
        for i in n[len(n)-1::-1]:
                m += i
        if (int(n) == int(m)):
                prime = "true"
                for j in range(2,int(n),1):
                        if ( int(n)%j == 0 ):
                                prime = "false"
                if ( prime == "true" ):
                        print(n)