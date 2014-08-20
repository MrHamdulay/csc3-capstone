height = eval(input("Enter the height of the triangle:\n"))
num=1
count=0
for i in range((2*height-1),0,-1):
    print(" "*(height-count-1),"*"*num,sep="")
    num+=2
    count+=1
    if count==height:
        break
    