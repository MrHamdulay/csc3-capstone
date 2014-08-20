#KNNSAD001#Assignment 8#Program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included)
import mathimport sys
sys.setrecursionlimit (30000) #high numbers can be used 
def pal(x,y): #set parameters to given variables- x and y
    if(len(str(x))!=1): #if the number hdoesnt have only one digit, come in
        d=x%10 #this gives the last number 
        y=y+str(d) #adds the last number to test
        return pal((x-(x%10))//10,y) #calls the function again of the number - the last digit
    else:
        return(y+str(x))

def prime(number,x,p):
    if(number==1):
        return (p+"Not")
    sq=int(math.sqrt(number)) #gets the sqrt of function
    if(x!=(sq+1)): # if it is not the srqrt
        if(number%x!=0): #if it is divisible
            return prime(number,x+1,p) #call function again
        else:
            return (p+"Not") #return not a prime
            
    
def method(a,number): 
    if a<=number:       #while number-a is not equal to number-n
        tespPal=int(pal(number,"")) #Pal function is called
        if tespPal==number: #number reversed is equal to the inserted number 
            testPrime=prime(number,2,"") #prime function is called
            if testPrime!="Not":
                print(number) 
        method(number+1,m) 
        
if __name__== "__main__":
    number=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    method(number,m)
    
    
    