import math
def main():
    x=math.sqrt(2)
    y=2
    while True:
        
        y=y*(2/x)
        x=math.sqrt(x+2)
        if x==2:
            break
    print('Approximation of pi:',round(y,3))
    radius=eval(input("Enter the radius: \n"))
    area= y*(radius)**2
    print('Area:',round(area,3))
    
main()