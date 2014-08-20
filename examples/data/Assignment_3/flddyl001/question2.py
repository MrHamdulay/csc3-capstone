def TriAngle():
    v_height = eval(input("Enter the height of the triangle:\n"))
    i = v_height - 1
    v_count = 1
    while i > -1:
        print(" "*i,"*"*v_count,sep="")
        i = i - 1
        v_count = v_count + 2
TriAngle()
