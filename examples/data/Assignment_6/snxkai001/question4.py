#kairav soni

marks0=[0,0,0,0,0]
marks=input("Enter a space-separated list of marks:\n")
mark=marks.split()

for i in range(len(mark)):
    symb=eval(mark[i])
    
    if(symb>=75):
        marks0[0]=marks0[0]+1
        
    elif(70<=symb<75):
        marks0[1]=marks0[1]+1
        
    elif(60<=symb<70):
        marks0[2]=marks0[2]+1
        
    elif(50<=symb<60):
        marks0[3]=marks0[3]+1
        
    else:
        marks0[4]=marks0[4]+1
        
print("1 |"+(marks0[0]*"X")+"\n2+|"+(marks0[1]*"X")+"\n2-|"+(marks0[2]*"X")+"\n3 |"+(marks0[3]*"X")+"\nF |"+(marks0[4]*"X"))
