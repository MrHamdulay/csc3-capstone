def graph():
    y = input('Enter a function f(x):\n')
    
    #fun = eval(y)
    for x in range(10,-11,-1):
        for j in range(-10,11):
            fun = round(eval(y))
            if x == fun:
                print('o',end='') 
    
            elif x == 0 and j == 0:
                print("+",end='')
            elif x == 0:# and i == 0:
                print('-',end='')#,'+','-'*10,sep='')    
            elif j == 0:
                print('|',end='')
            else:
                print(" ",end='')
        
        print()
         #   elif i == func:
               # func = eval(y)
              #  x+=1
        #print() 
#
graph()