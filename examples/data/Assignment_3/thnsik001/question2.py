#Assignment 3
#22/03/2014
#q2
#thnsik001

def tri(height):
    i=0
    while i!=height:
        if height==(i+1):
            print("*"*(height*2-1))
        else:
            print((height-(i+1)-1)*" ","*",end="")
            print(i*2*"*")        
        i+=1    
        

height = eval(input("Enter the height of the triangle:\n"))
tri(height)