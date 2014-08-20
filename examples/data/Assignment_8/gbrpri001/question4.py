"""Priyanka Goberdhan
Question four - Assignment 8"""

import sys
sys.setrecursionlimit (30000)


def check_pal(x):
        if(x<10):
                return True
                
        else:
                if((x//(10**(len(str(x))-1)))==(x%10)):
                        return check_pal((((x-((x//(10**(x%10)))*(10**(len(str(x))-1))))-(x%10))/10)-(((((x-((x//(10**(x%10)))*(10**(len(str(x))-1))))-(x%10))/10))//10)**10)#
                else: 
                                                
                        return False
count=2      

def check_pri(n):
        global count
        if(n<2):
                return False
        else:
                                
                if(n==2):
                        return True
                else:
                                                
                        if count==(n//2)+1:
                                return True
                        else: 
                                if(n%count==0):
                                        return False
                                else:
                                        count=count+1
                                        return check_pri(n)
                                                             
def find(start_pal,end_pal):
        global count
        count=2
        if start_pal == end_pal+1:
                return True
        else:
                if check_pal(start_pal):
                        if check_pri(start_pal):
                                print(start_pal)
                                    
                start_pal=start_pal+1
                find(start_pal,end_pal)
                                
                                

start_pal = eval(input("Enter the starting point N:\n"))

end_pal = eval(input("Enter the ending point M:\n")) 

print("The palindromic primes are:")

find(start_pal,end_pal)                                
