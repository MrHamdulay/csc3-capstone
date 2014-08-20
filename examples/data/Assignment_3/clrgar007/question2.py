#question2.py
height=eval(input("Enter the height of the triangle:\n"))
def triangle(height):
    gap=height-1 #This is what it looked like in assignment
    i=1
    while i<=height:
        print(gap*" ","*"*(2*i-1),gap*" ",sep="")        
        i+=1 #increasing so that it becomes increasingly close to the value of the height
        gap=gap-1 #decreasing the gap so that it fits the increasing triangle

triangle(height)