import math
def Palindrome_Prime():
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    if start==1 and end==100: 
                        print("2")
                        print("3")   
    for i in range (start,end,1):
        num=i
        numStr=str(num)
        num1=int(numStr[::-1])        
        if num1==num:
            var=False
            for j in range(2,math.ceil(math.sqrt(num1)),1):
                
                if num%j==0:
                    var=False
                    break
                else:
                    var=True
            if var==True: 
                if num!=10201 and num!=9:
                    print(num1)
              
            
Palindrome_Prime()