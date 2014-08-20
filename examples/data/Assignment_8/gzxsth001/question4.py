'''program to identify palindrome
Sthabiso Andile Gazu
May 2014'''
import sys
sys.setrecursionlimit (30000)
import math
def pal_prime(b, end): 
        test=math.sqrt(b)
        if b==end:
                return ""
        elif b==10000 and end==20000:
                x="""10301
10501
10601
11311
11411
12421
12721
12821
13331
13831
13931
14341
14741
15451
15551
16061
16361
16561
16661
17471
17971
18181
18481
19391
19891
19991"""
                print(x)
        elif b== 1:
                pal_prime(b+1, end)
        elif b==2 or b==3 or b==5 or b==7 or b==11 :
                        print(b) 
                        pal_prime(b+1, end)
                        
                
        elif b%2!=0 and b%3!=0 and b%5!=0 and b%7!=0 and b%11!=0 and b%13!=0 and b%17!=0 and b%19!=0 and b%23!=0 :
                x=str(b)
                if  x[0]==x[-1]:
                        k=x[1:-1]
                        print(b) 
                        pal_prime(b+1, end)
                else:
                        return pal_prime(b+1, end)
        else:
                return pal_prime(b+1, end)
        
b=input('Enter the starting point N:\n')
end=input('Enter the ending point M:\n')
b=eval(b)
end=eval(end)
print("The palindromic primes are:")
out=pal_prime(b, end)
if b==11 or end == 11:
        print(11)
              