
#Suvir Gajadhur
#Function to create a hollow box comprimising of stars '*'



def print_square():
    
    print ("*****")
    print ("*   *")
    print ("*   *")
    print ("*   *")
    print ("*****")
    
def print_rectangle(width,height): 
    
    print ("*"*width)                      
    for i in range(0,height-2):            
        print("*"+" "*(width-2)+"*")         
    print ("*"*width)                      
    

def get_rectangle(width,height): 
    
    first_line="*"*width+"\n"                        
    bottom_line="*"*width                            
    body=("*"+(width-2)*" "+"*\n")*(height-2)         
    rectangle_string= (first_line+body+bottom_line)  
    return(rectangle_string)

get_rectangle(6,7)