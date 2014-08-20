message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

i=1
numdashes=len(message)+(2*thickness)
dash="-"*numdashes
border=("+"+dash+"+")
step=1
end=""
while(i<=thickness):    
    print(border)
    end=border+"\n"+end
    numdashes-=2
    dash="-"*numdashes
    border=("|"*step+"+"+dash+"+"+"|"*step)
    i+=1
    step+=1
t=1
while(t<=repeat):
    print(("|"*thickness)+" "+message+" "+("|"*thickness))
    t+=1
i=1
print(end)