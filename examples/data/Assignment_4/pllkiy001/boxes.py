def print_square():

    for i in range (0,5,1):

        if i==0 or i==4:

            print("*****")

        else:

            print("*   *")




def print_rectangle(width,height):

    for i in range (0,height,1):

        if i==0 or i==height-1:

            print("*"*width)

        else:

            print("*"," "*(width-2),"*",sep="")




def get_rectangle(width,height):

    

    x=""

    for i in range (0,height,1):

        

        if i==0 or i==height-1:

            x=x+"*"*width

            x=x+"\n"

        else:

            s="*"

            d=" "*(width-2)

            x=x+s+d+s

            x=x+"\n"

    return x