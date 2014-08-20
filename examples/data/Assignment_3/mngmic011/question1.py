#question 1
#Micaela Menegaldo

height=eval(input("Enter the height of the rectangle: \n"))
width=eval(input("Enter the width of the rectangle: \n"))
def rectangle(width,height):
    for i in range(0,height):
        print("*"*width)
   
        
if __name__=='__main__':
    rectangle(width,height)