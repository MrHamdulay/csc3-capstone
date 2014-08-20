x=[0,0,0,0,0]

enter=input("Enter a space-separated list of marks:\n")

mark=enter.split()

for i in range(len(mark)):
    sub=eval(mark[i])
    
    if(sub>=75):
        x[0]+=1
        
    elif(70<=sub<75):
        x[1]+=1
        
    elif(60<=sub<70):
        x[2]+=1
        
    elif(50<=sub<60):
        x[3]+=1
        
    else:
        x[4]+=1
        
print("1 |"+(x[0]*"X")+"\n2+|"+(x[1]*"X")+"\n2-|"+(x[2]*"X")+"\n3 |"+(x[3]*"X")+"\nF |"+(x[4]*"X"))
