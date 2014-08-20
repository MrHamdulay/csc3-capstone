import math.sqrt

global end

def prime(number,i):
    
        
    if number%2==0:
        prime(number+1,i)
    elif number>end:
        
    elif i< math.sqrt(number):
        if number%i==0:
            prime(number+1,2)
        
        else:
            prime(number,i+1)
            
    if(palin(number) == True):
        print(number)
        
    else:
        prime(number+1, 2)
    

def palin(s):
    if s == '':
            return True
        else:
            if ((s[0]) - (s[len(s)-1])) == 0:
                # v-- forgot this here
                return palin(s[1:len(s)-1])
            else:
                return False           
def main():
    x=input("Enter the starting point N:\n")
    y=input("Enter the ending point M:\n")
    
    end = y
    
    prime(x, 2)
    
    
    