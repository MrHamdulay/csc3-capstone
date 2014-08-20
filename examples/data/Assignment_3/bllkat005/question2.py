#BLKAT005
#Kate Bell
# 23 March 2014

height = eval(input("Enter the height of the triangle:\n"))
for i in range(height):
    starnum=1+i*2
    gap=(1+(height-1)*2-starnum)//2
    print(gap*" ","*"*starnum,gap*" ",sep="")
    
    