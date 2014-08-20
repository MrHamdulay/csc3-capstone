import math
start1 = eval(input("Enter the starting point N: \n"))
start = start1 + 1
end = eval(input("Enter the ending point M: \n"))
range1 = end -start

string1= ""
string2= ""
print("The palindromic primes are:")




for i in range (range1):
    if(start>=2):
        
        prime = True
        for d in range(2,start//2+1):
            if(start%d==0):
                prime = False
               
        
   
        
        string1 = str(start)
        string2 = string1[-1::-1]
        if(prime == True):
            if (string1 == string2):
                print(string1)
            else:
                print("", end = "")
       
        start = start +1
        
    else:
        start = start + 1
           
            

   
   
        