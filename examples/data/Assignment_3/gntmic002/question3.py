#assignment 3.3

m = " " + input("Enter the message:\n") + " "
c = eval(input("Enter the message repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))

w = len(m) + 2*t
l = 2*t + c 

hor = 0
for k in range(1,t+1):
    ans = ""
    for j in range(1, w+1):
        if (j<=hor) or (j>w-hor):
            ans = ans + "|"
            
        elif (j==1+hor) or (j==w-hor):
            ans = ans + "+"
        else:
            ans = ans + "-"
    print(ans)
    hor+=1
            
    

for k in range(1, c+1):
    ans = ""
    for j in range(1, t+1):
        ans = ans + "|"
       
    ans = ans + m
    
    for j in range(1, t+1):
        ans = ans + "|"
        
    print(ans)

hor = t-1
for k in range(1,t+1):
    ans = ""
    for j in range(1, w+1):
        if (j<=hor) or (j>w-hor):
            ans = ans + "|"
                
        elif (j==1+hor) or (j==w-hor):
            ans = ans + "+"
        else:
            ans = ans + "-"
    print(ans)
    hor-=1           
            
        
        
    
               

         