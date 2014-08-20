#GLMSUM001
#Sumayah Goolam Rassool
#Q_1


def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
       

def get_rectangle(width,height): 
    
    
    display=""
    
    for i in range(1,height+1): 
        
        if i==1:
            
            display+=("*"* width + "\n")
            
        elif i == height: 
            
            display+=("*"* width) 
            
        else:
            
            display+=("*" +(" "*(width-2))+"*"+"\n")
            
    return display

def print_rectangle(width,height): 
    
    print(get_rectangle(width,height))