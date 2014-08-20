#height=eval(input("Enter the height of the triangle:\n"))
#gap=height
#for i in range(1,2*height,2):
    #if gap>0:
        #print(gap*" ","*"*i)
    #gap-=1

height=eval(input("Enter the height of the triangle:\n"))
gap=(height-2)
for i in range(1,(2*height),2):
    if height==1:
        print("*")
    else:
        print(gap*" ",end=" ")
        print("*"*i)
        gap-=1
        z=i
        if gap==-1:
            break
if height>1:
    print("*"*(z+2))
