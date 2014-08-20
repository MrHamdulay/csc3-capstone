#Question2 
#Assignment3
#Tase Ngambi

def drawTriangle():
    height = eval(input("Enter the height of the triangle:\n"))
    newHeight = height
    
    incre = 1
    for i in range(newHeight):
        print(" "*(newHeight-i-1), end ="")
        print("*"*incre)
        incre = incre+2
      
        
             
drawTriangle()       
        
                  
                  