def print_rectangle(width, height):
       for i in range (height):
              for j in range (width):
                     if (i == 0 or i == height-1) :
                            print("*", end = "")
                     elif (j == 0 or j == width-1):
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
              
def get_rectangle(width, height):
       rect = ""
       for i in range (height):
              for j in range (width):
                     if (i == 0 or i == height-1) :
                            rect+="*"
                     elif (j == 0 or j == width-1):
                            rect+="*"
                     else:
                            rect+=" "
              rect += "\n"
              
       return rect
              
              