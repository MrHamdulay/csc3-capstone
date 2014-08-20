height=eval(input("Enter the height of the triangle:\n"))

stopcount= height+(height-1)
count=1
space=" "
countspace=height-1
while count<stopcount+1:
    print(space*countspace,"*"*count,sep="")
    count=count+2
    countspace=countspace-1
    