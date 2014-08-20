marx=[0,0,0,0,0]

enter=input("Enter a space-separated list of marks:\n")

mark=enter.split()

for i in range(len(mark)):
    sub=eval(mark[i])
    
    if(sub>=75):
        marx[0]+=1
        
    elif(70<=sub<75):
        marx[1]+=1
        
    elif(60<=sub<70):
        marx[2]+=1
        
    elif(50<=sub<60):
        marx[3]+=1
        
    else:
        marx[4]+=1
        
print("1 |"+(marx[0]*"X")+"\n2+|"+(marx[1]*"X")+"\n2-|"+(marx[2]*"X")+"\n3 |"+(marx[3]*"X")+"\nF |"+(marx[4]*"X"))
