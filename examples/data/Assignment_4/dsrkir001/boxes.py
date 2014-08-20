def print_square():
    for i in range(5):
        for j in range(5):
            if (i==0 or i==4 or j==0 or j==4):
                print("*",end='')
            else:
                print(" ",end='')
        print()

def print_rectangle(wide,height):
    for i in range(height):
            for j in range(wide):
                if (i==0 or i==(height-1) or j==0 or j==(wide-1)):
                    print("*",end='')
                else:
                    print(" ",end='')
            print()   
            
def get_rectangle(wide,height):
    a=""
    for i in range(height):
                for j in range(wide):
                    if (i==0 or i==(height-1) or j==0 or j==(wide-1)):
                        a+="*"
                    else:
                        a+=" "
                a+="\n"
    return a