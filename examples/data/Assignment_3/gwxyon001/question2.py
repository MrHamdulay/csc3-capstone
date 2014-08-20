
#module

def tri(par1):
    gap=par1-1 #we need // here - why?
    inc=0
    for i in range(1,par1+1):
        print(' '*gap,end='')
        print('*'*(i+inc))
        gap-=1 
        inc+=1
        

h=eval(input("Enter the height of the triangle:\n"))
tri(h)

