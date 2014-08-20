#Aiden Walton
#WLTAID001
#Program to draw a triangle

def tri():
    gap=par1-1
    for i in range(0,2*(par1),2):
        print(gap*' ',end="")
        print('*'*(i+1))
        gap=gap-1
        
if __name__=="__main__":
    par1=0
    par1=eval(input("Enter the height of the triangle:\n"))
    tri()
