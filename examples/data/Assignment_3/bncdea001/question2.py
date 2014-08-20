def triangle():
    h=eval(input("Enter the height of the triangle: \n"))
    star=-1
    #h=h-1
    for i in range(h):
        star=star+2
        print(" "*(h-1), "*"*star, sep="")
        h=h-1
triangle()
