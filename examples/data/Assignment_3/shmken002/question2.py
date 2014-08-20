#isoceles triangle of a given height using the ‘*’ character
#ringo shima
#24/03/14
height = eval(input("Enter the height of the triangle:\n"))

def tri():
        for i in range(0,height,1):
                x= (2*(i)+1)
                x=x*"*"
                print(" " * (height-1-i)+ x.format("*"))
tri()
