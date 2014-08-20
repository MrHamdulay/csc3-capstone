#x=input("Choose test:\n")
def print_square():
    print ("*****")
    print ("*   *")
    print ("*   *")
    print ("*   *")
    print ("*****")

def print_rectangle(width, height):
    print ("*"*width)
    for i in range (height-2):
        print("*", " "*(width-2), "*", sep="")
    print ("*"*width)
    
def get_rectangle(width, height):
    a=""
    a+="*"*width
    for i in range (height-2):
        a+="\n"+"*"+" "*(width-2)+"*"
    a+="\n"+"*"*width    
    return(a)

#if x=="a":
    #print_square()
#elif x[0]=="b":
    #print_rectangle(int(x[2]),int(x[4]))
#elif x[0]=="c":
    #get_rectangle(int(x[2]),int(x[4]))