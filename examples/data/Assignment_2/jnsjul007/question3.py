def main():
    import math
    a=math.sqrt(2)
    
    b=2
    while True:
        b=b*(2/a)
    #while True: 
        a=math.sqrt(2+a)
        if a==2:
            break
    
       
    print("Approximation of pi:", round(b,3)) 
    x=eval(input("Enter the radius:\n"))
    area=b*(x**2)
    print("Area:",round(area,3))


main()