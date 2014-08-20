height = int(input("Enter the height of the triangle:\n"))
for i in range(1,height+1):
    st = 2*i-1
    sp = height-i
    print(sp*" "+st*"*")
