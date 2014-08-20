# Drawing an isoceles triangle 
# Monwabisi Dingane
# 24 March 2014

def isoceles(hight):
    for j in range(0,(hight)+2,1):
        for i in range((hight),0,-1):
            if i != j:
                print(" ",end='')
            else:    
                print("*"*i,end='')
                print("*"*(i-1),end='')
        print()
        

h = eval(input("Enter the height of the triangle:\n"))
isoceles(h)