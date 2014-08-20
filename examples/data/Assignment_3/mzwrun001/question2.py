t=eval (input ("Enter the height of the triangle:""\n"))
gap=(t-1)
for i in range (1,t*2,2):
    print(" "*gap,"*"*i,sep="")
    gap-=1
    
