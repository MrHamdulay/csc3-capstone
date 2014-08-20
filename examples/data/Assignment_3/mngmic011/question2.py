#question 2
#Micaela Menegaldo

height=eval(input("Enter the height of the triangle: \n"))

def triangle(height):
    star='*'
    gap=(height-1)
    for i in range(1,height+1):
        print(gap*' ',"*"*(i*2-1),gap*' ',sep='')
        gap=gap-1
        
        
        
if __name__=='__main__':
    triangle(height)