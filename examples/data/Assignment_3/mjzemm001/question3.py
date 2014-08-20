m = str(input("Enter the message:\n")) #message a user must enter and I converted it to a string
mcr = eval(input("Enter the message repeat count:\n")) #how many times must the message repeat itself
ft = eval(input("Enter the frame thickness:\n")) #the frame thickness
m1 = len(m) #calculate the lenght of m
sy1 = (2*ft) #sy2 = len(str(sy1))
s1 = (" "*2)
s2 = len(str(s1))
l = m1 + sy1 + s2
#print("m1=",m1,"sy1=",sy1,"s2=",s2,"l=",l)
      
def introduction(): # this is a top part in the frame
    a = 1 #set the base variable
    b = 0
    c = 1    
    while a <= ft:
        print ("|"*b,"+"*c,"-"*(l-(2*(b)+2*(c))) ,"+"*c,"|"*b,sep= "")
#        print("|","+","-"*(l-4) ,"+","|",sep="")
        a+= 1 #this will add 1 to the content in the base varible until the loop stop
        b+= 1
        
    
def body(): # this is a message part in the frame
    message = 1
    while message <= mcr :
        print("|"*ft,m,"|"*ft,sep=" ")  
        message += 1 #this will add 1 to the content in the base varible stop
        
def conclusion(): # this is the bottom part of the frame
    d = 1 #set the base variable
    e = (ft-1)
    f = 1    
    while d <= ft:
        print ("|"*e,"+"*f,"-"*(l-(2*(e)+2*(f))) ,"+"*f,"|"*e,sep= "")
        d+= 1
        e = e -1 #this will add 1 to the content in the base varible stop
#    print ("+","-"*(l-2) ,"+",sep="")
        
introduction() #invoke the defined function
body() #invoke the defined function
conclusion() #invoke the defined function