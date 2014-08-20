# question4.py 
# a program to find all palindromic primes between two integers supplied as input 

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
for i in range(N+1,M): 
    d=i
    number=""
    while d!=0:
        number = number + str(d%10)
        d = d//10
    number=int(number)

    if number==i:                 #Palindromic number
        prime = "true"
        for j in range(2,(i)):
            if i%j==0:
                prime = "False"
                break
            
        if prime == "true":
            print(i)
            
             
        
            
                
            
        
    
    
    
    