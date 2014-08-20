




def print_square():
               print("*"*5)
               print("*   *\n"*3, end="")
               print("*"*5)
                        
                   
          
        

def print_rectangle (width, height):
               
               z = width - 2
               y = height - 2                   
               print("*"*width)
               for i in range(y):
                              print("*" + " " *z +"*", end = "\n")
               print("*"*width)            

            


def get_rectangle (width, height):
               boxStr = "" 
               z = width - 2
               y = height - 2                   
               boxStr += ("*"*width)+"\n"
               for i in range(y):
                              boxStr +=("*" + " " *z +"*" +"\n")
               boxStr += ("*"*width) 
               return  boxStr