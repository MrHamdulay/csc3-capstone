def print_square():
 print ("*"*5)
 for i in range(0,5-2):
  print('*' + ' '*(5-2) + '*')
 print ("*"*5)



def print_rectangle(width, height):
 print ("*"*width)
 for i in range(0,height-2):
  print('*' + ' '*(width-2) + '*')
 print ("*"*width)


def get_rectangle(width,height):
    bb=""
    bb+="*"*width + "\n"
    for i in range(height-2):
        bb+="*" + " "*(width-2) + "*" + "\n"
    bb+="*"*width + "\n"
    return bb
