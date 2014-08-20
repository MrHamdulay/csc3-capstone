#Tayla George
#Program for isoceles triangle
#26 March 2014

h = eval(input("Enter the height of the triangle:\n"))
         
def triangle():
    for i in range(1,h+1):
        a = h -i
        print(a*" ","*"*i,"*"*(i-1),sep="")
        
triangle()
    
    
    