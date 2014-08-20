def print_square():      
        print("*"*5)
        for i in range(5-2):
                print("*"," "*(5-2),"*",sep="")
        print("*"*5)


def print_rectangle(width,height):
        print("*"*width)
        for i in range(height-2):
                print("*"," "*(width-2),"*",sep="")
        print("*"*width)
        
        
def get_rectangle(width,height):
        w="*"*width
        for i in range(height-2):
                h="*"+" "*(width-2)+"*"
        p=w+'\n'+((h+'\n')*(height-2))+w
        return p
        


                
                
        
        
        
                
                
        
    
    
           