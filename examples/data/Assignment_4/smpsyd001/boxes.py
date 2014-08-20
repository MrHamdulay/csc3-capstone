def print_square():
    for i in range (5):
        if i==0 or i==4:
            print ("*****")
        else: 
            print("*   *")
            
def print_rectangle(a,b):
    #width=a height=b
    for i in range(b):
        if i==0 or i==(b-1):
            print ("*"*a)
        else:
            print ("*",' '*(a-2),"*",sep='')
            
def get_rectangle(a,b):
    p=''
    for i in range(b):
        if i==0 or i==(b-1):
            p+=("*"*a+"\n")
        else:
            p+= ("*"+' '*(a-2)+"*"+"\n")
    return p

    
    