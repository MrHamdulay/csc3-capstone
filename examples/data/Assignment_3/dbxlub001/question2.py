def triangle():
    i=(0)
    hieght=eval(input("Enter the height of the triangle:\n"))
    gap=(hieght*2//2)
    for i in range(0,(hieght*2)-1,2):
        #gap=(2*hieght//2)
        print(' '*(gap-1),end='')
        print("*"*(i+1), end="\n")
        gap=(gap-1)
triangle()