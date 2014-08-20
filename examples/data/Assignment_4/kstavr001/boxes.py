def print_rectangle(w,h):
       for i in range (h):
              for j in range (w):
                     if (i == 0 or i == h-1) :
                            print("*", end = "")
                     elif (j == 0 or j == w-1):
                            print("*", end = "")
                     else:
                            print(" ", end = "")
              print()




def print_square():  
       for i in range (5):
              for j in range (5):
                     if (i == 0 or i == 4) :
                            print("*", end = "")
                     elif (j == 0 or j == 4):
                            print("*", end = "")
                     else:
                            print(" ", end = "")
              print() 
              
def get_rectangle(w,h):
       shape = ""
       for i in range (h):
              for j in range (w):
                     if (i == 0 or i == h-1) :
                            shape+="*"
                     elif (j == 0 or j == w-1):
                            shape+="*"
                     else:
                            shape+=" "
              shape += "\n"
              
       return shape
              
              