a,b,c,d=eval(input("Enter the height of the triangle:\n"))," ","*",0
while d<a:
    print((a-(d+1))*b,c*((2*d)+1),sep="")
    d+=1