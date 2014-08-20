h=eval(input("Enter the height of the triangle:\n"))
gap=" "*(h-1)
star="*"
for i in range(h):
    print(gap,star,sep="")
    gap=" "
    h=h-1
    gap=gap*(h-1)
    star=star+"**"