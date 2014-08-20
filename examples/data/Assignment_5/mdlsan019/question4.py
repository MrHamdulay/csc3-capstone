# Question4
# Sanele Mdlalose
# MDLSAN019
# 16-04-2014
import math
f_of_x=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        f=list(f_of_x)
        for i in range (len(f_of_x)):
            if f[i]=="x":
                f[i]='('+str(x)+')'
                
            ans=round(eval(''.join(f)))
            
    
        if x==0 and y==0:
            if y!=(ans):
                print('+',end='')
            else:
                print('o',end='')
        elif x==0:
            if y==ans:
                print('o',end='')
            else:
                print('|',end='')
        elif y==(ans):
            print('o',end='')
        
        elif y==0:
            print('-',end='')
         
        else:
            print(' ',end='')
    print()        
            
            
        
