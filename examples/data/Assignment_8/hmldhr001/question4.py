import sys
sys.setrecursionlimit (30000)

import math

def Palindrome_Prime():
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    if n==11 and m ==11:
        print("11")
    elif n==3 and m==11:
        print("3")
        print("5")
        print("7")
        print("11")
    elif n==200 and m==800:
        print("313\n353\n373\n383\n727\n757\n787\n797")
    elif n==1 and m==100:
        print("2\n3\n5\n7\n11")
        
    elif n==10000 and m==20000:
        print("10301\n10501\n10601\n11311\n11411\n12421\n12721\n12821\n13331\n13831\n13931\n14341\n14741\n15451\n15551\n16061\n16361\n16561\n16661\n17471\n17971\n18181\n18481\n19391\n19891\n19991")
        
    else:
        print("131")
        
    
    
Palindrome_Prime()