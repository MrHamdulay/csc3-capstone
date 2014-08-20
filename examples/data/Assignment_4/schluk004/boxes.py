def print_square():
 print("*****")
 for i in range(3):
  print("*   *")
 print("*****")
 
def print_rectangle(width,height):
 print("*"*width)
 for i in range(height-2):
  print("*"," "*(width-2),"*",sep="")
 print("*"*width)
 
def get_rectangle(width,height):
 rec=("*"*width)+"\n"
 for i in range(height-2):
  rec+="*"+" "*(width-2)+"*\n"
 rec+=("*"*width)
 return(rec)
