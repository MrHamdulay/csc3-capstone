def Draw_Frame():
    v_message = input("Enter the message:\n")
    v_repeat = eval(input("Enter the message repeat count:\n"))
    v_thick = eval(input("Enter the frame thickness:\n"))
    v_dash = len(v_message) - 1
    i = v_thick
    x = v_thick
    j = 0
    y = v_thick - 1
    #v_line = v_repeat - 1
    
    while i > 0:
        print("|"*j,"+","-"*(v_dash + (i*2)+1),"+","|"*j,sep="")
        i = i - 1
        j = j + 1

    while v_repeat > 0:
        print("|"*v_thick," ",v_message," ","|"*v_thick,sep="")
        v_repeat = v_repeat - 1
        
    while x > 0:
        print("|"*y,"+","-"*(v_dash + 3),"+","|"*y,sep="")
        v_dash = v_dash + 2
        x = x - 1
        y = y - 1
Draw_Frame()