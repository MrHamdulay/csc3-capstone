#Shivan Gopee
#4/04/2014
#Question 1

def print_square():           #function called when user inputs "a"
    print ("*"*5)             #print top of square
    for i in range (3):       #print sides of square
        print ("*"," "*3,"*",sep="")
    print ("*"*5)      
    

def print_rectangle(width,hight):      
    print ("*"*width)                  
    for i in range (hight-2):          
        print ("*"," "*(width-2),"*",sep="")
    print ("*"*width)                  


def get_rectangle(width,hight):        
    x=("*"*width+"\n")+(("*"+" "*(width-2)+"*"+"\n")*(hight-2))+("*"*width) 
    return x