#Michael_Odhiambo
#ODHMIC003
n= eval(input("Enter the starting point N:"'\n'))
m= eval(input("Enter the ending point M:"'\n'))
print("The palindromic primes are:") 

for i in range(n,m):
    if (i>10 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%9!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 or i==11 or i==13 or i==17 or i==19 and i!=m and i!=n and i%23!=0 and i%29!=0 and i%31!=0 and i%37!=0 and i%41!=0 and i%43!=0 and i%47!=0 and i%53!=0 and i%59!=0 and i%61!=0 and i%67!=0 and i%71!=0 and i%73!=0 and i%79!=0 and i%83!=0 and i%89!=0 and i%97!=0 ) or (1<i<10 and i%2!=0 and i%3!=0 or i==2 or i==3 and i!=m and i!=n): 
        x = i
        y = int(str(i)[::-1])
        if x%y==0:
            print(x)
            
            