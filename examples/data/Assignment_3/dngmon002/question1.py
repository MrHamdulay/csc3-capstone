# Drawing a rectangle
# Monwabisi Dingane
# 24 March 2014

def rectangle(hight,wigth):

    for i in range(hight):
        for j in range(wigth):
            print("*",end="")
        print()
          
h = eval(input("Enter the height of the rectangle:\n"))
w = eval(input("Enter the width of the rectangle:\n"))

rectangle(h,w)