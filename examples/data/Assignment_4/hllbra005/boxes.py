#Question1 boxes.py 
#Brandon Hall (HLLBRA005)
#4 April 2013


def all(width , height): 
    
    rectangle = ""
        
    for i in range(height): # Ranges up until the height, i.e The rows     
            
        if(i == 0): # top
            rectangle =rectangle + ( "*" * (width) + "\n")
            
        elif(i == (height-1)):   #bottom 
            rectangle =rectangle + ( "*" * (width) )
            
        else: #mid-row/s
            rectangle = rectangle + ("*" + (" " * (width-2) ) + "*" + "\n")
              
            
    return rectangle 

def print_square ():
    
    width = 5
    height = 5

    print(all(width , height))
    
def print_rectangle (width, height):
    
    print(all(width , height))

def get_rectangle(width, height):
    
    
    rectangle = all(width,height)
    
    return rectangle 