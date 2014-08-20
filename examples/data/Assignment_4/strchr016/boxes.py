"""Christopher Sterley
Program for different boxes
31/3/2014"""
def print_square ():
    print("*"*5)
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"*5)

def print_rectangle (width, height):
      print("*"*width)
      for i in range (height-2):
        print("*"," "*(width-2), "*",sep="")
      print("*"*width)

def get_rectangle (width, height):
     return ("*"*width)+"\n"+(height-2)*(("*"+" "*(width-2)+"*")+"\n")+("*"*width)