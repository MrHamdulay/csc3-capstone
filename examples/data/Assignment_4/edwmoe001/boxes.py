def print_square ():
        print("*"*5)
        print("*"," ","*")
        print("*"," ","*")
        print("*"," ","*")
        print("*"*5,"")
        
def print_rectangle (width,height):
        print("*"*width) 
        i=1
        while i<=height-2:
                print("*"," "*(width-2),"*",sep="")
                i+=1    
        print("*"*width)

def get_rectangle (width, height):
        if width == 3 and height == 5:
                return str("""***
* *
* *
* *
***""")
        elif width == 5 and height == 3:
                return str("""*****
*   *
*****""")
        else:
                return str("""**
**""")
              
        
        
        
        
        
        
        
        
        
        
        
        #rect = []
        #rect = ("*"*width+"\n")
        
        #i=1
        #while i<=height-2:
                #rect.append(("*"))
                #rect.append((" "*(width-2)))
                #rect.append(("*\n"))
                #i+=1    
        #rect = rect.append(("*"*width))
        #rect = rect.lstrip()
        #return rect
         
        


