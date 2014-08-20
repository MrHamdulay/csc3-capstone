#Question 3, The Frame Issue

def main():
    mes=input("Enter the message: \n")
    rep=eval(input("Enter the message repeat count: \n"))
    thick=eval(input("Enter the frame thickness: \n"))
    
    if thick==1:
        print("+", (len(mes)+(2*thick))*"-", "+", sep="")
    
    #for i in range (thick):
     #   print("+", (len(mes)+(2*thick))*"-", "+", sep="")
        
    elif thick>1:
        x=thick
        temp=x
        for i in range (x):
            print((x-temp)*"|" ,"+", (temp-1)*"-", (len(mes)+2)*"-", (temp-1)*"-", "+", (x-temp)*"|", sep="")
            temp=temp-1
    
    
    for i in range(rep):
        print("|"*(thick), " ", mes, " ", "|"*(thick), sep="")
       
     
    #if thick==1:
     #       print("+", (len(mes)+(2*thick))*"-", "+", sep="")     
    
    x=thick
    temp=0
    for i in range(x-1,-1,-1):
        temp=temp+1
        print((x-temp)*"|" ,"+", (temp-1)*"-", (len(mes)+2)*"-", (temp-1)*"-", "+", (x-temp)*"|", sep="")
            
        

main()
