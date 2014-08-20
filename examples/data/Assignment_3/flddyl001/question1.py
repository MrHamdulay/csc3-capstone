def RectAngle():
    v_height = eval(input("Enter the height of the rectangle:\n"))
    v_length = eval(input("Enter the width of the rectangle:\n"))
    while v_height>0:
        print("*"*v_length)
        v_height = v_height - 1
RectAngle()            