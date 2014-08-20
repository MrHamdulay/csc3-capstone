def print_square():
  print("*****")
  print("*   *")
  print("*   *")
  print("*   *")
  print("*****")
  
def print_rectangle(width,height):
  print("*"*width)
  for i in range(height-2):
    print("*"," "*(width-2),"*",sep="")
  print("*"*width)
    
def get_rectangle(width,height):
    stringbox=""
    for i in range (0,height,1):
        if i==0 or i==height-1:
            stringbox=stringbox+"*"*width
            stringbox=stringbox+"\n"
        else:
            s="*"
            d=" "*(width-2)
            stringbox=stringbox+s+d+s
            stringbox=stringbox+"\n"
    return stringbox