height = eval(input("Enter the height of the triangle:\n"))

i=1
t=1
gap=" "*(height-1)
gapheight = height-1
while(i<=height):
    print(gap,"*"*t,sep="")
    i+=1
    gapheight-=1
    gap=" "*gapheight
    t+=2