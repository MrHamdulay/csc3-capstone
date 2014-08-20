def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
        
    print("*****")
    

def print_rectangle(x,y):
    print("*"*x)
    for i in range(y-2):
        print("*"+" "*(x-2)+"*")
        
    print("*"*x)
    
    
def get_rectangle(a,z):
   
    pic=""
    for i in range(z):
            if(i==0) or (i==(z-1)):
                pic= pic+ (a*"*")
             
            else:
                pic= pic+("*"+(a-2)*" "+"*")   
                
            pic= pic+ "\n"
    return pic               
            
                
            
            
  
