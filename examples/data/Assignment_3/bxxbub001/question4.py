def prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def pala(num1,num2):
    #currNum =0
    print("The palindromic primes are:")
    for i in range(num1+1,num2):
        currNum= i
        if prime(i)== True:
        
        
            StringNum = str(currNum)
            revNum = StringNum[::-1]
        
            if revNum==StringNum:
                if currNum == 4:
                    print("",end="")
                else:   
                    print(revNum,end="\n")
            
            else:
                print("",end="")
        #print("Here",i)
            
            
bot= eval(input("Enter the starting point N:\n"))
top = eval(input("Enter the ending point M:\n"))
pala(bot,top)
