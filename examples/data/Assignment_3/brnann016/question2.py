height = eval(input ("Enter the height of the triangle:\n"))
m=height-1
for i in range(1,height+1,1):
    print(m*" "+"*"*(2*i-1))
    m=m-1