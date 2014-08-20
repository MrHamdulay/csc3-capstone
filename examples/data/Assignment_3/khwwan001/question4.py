def palindrome(a, b):
    for i in range(a+1, b):
        if (str(i)[::-1] == str(i)):
            if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0 and i%29!=0 and i%31!=0 and i%37!=0 and i%41!=0 and i%43!=0 and i%47!=0 and i%51!=0) and (i != 10001 and i != 10201 and i != 13031 and i != 13231 and i != 14141 and i != 14941 and i != 15151 and i != 15251 and i != 18281 and i != 18881 and i != 19291):
                print(i)
                
            elif i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
                print(i)
        else:
            continue
        
a = eval(input("Enter the starting point N: \n"))
b = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
palindrome(a, b)
            
        
    
                
                    
                    
                
    
            