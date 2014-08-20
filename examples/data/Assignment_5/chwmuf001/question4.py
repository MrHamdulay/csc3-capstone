import math

def graph():
    function = input("Enter a function f(x):\n")
    #f
    for y in range (10,-11,-1):
        for j in range (-10,11):
            x=j
            ans=round(eval(function))
            if ans==y:
                print('o',end='')
                
            elif j==0 and y==0:
                print('+',end='')
                
            elif j==0:
                print('|',end='')
                
            elif y==0:
                print('-',end='')
                
            else:
                print(' ',end='')
        
        print()
            
if __name__=='__main__':
    graph()


            
            
            
    
    
    
                     