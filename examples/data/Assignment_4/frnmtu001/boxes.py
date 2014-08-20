def print_square():
     print("*****")
     for i in range(3):
          print("*   *")
     print("*****")
def print_rectangle(width,height):
     x=" "
     print("*"*width)
     for i in range(1,height-1):
          print("*",x*(width-2),"*",sep="")
     print("*"*width)
def get_rectangle(width,height):
     a=" "
     c="*"*width+"\n"
     for i in range(1,height-1):
          c+="*"+a*(width-2)+"*"+"\n"
     c+="*"*width
     return c