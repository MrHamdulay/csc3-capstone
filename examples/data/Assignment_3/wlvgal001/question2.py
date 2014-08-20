#question2

def a(star):
        height=eval(input("Enter the height of the triangle:\n"))
        gap=(2*height-1)//2 
                
        for i in range(0,2*height,2):
               print(' '*gap,end='') 
               print(star*(i+1))
               gap=gap-1 

a("*")

    
