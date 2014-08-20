# boxes.py
#   print_square()
#     prints 5x5 box on the screen
#   print_rectanle(width,height)
#     prints a box on screen with given width and height
#   get_rectangle(width,height)
#     returns a string containing box with given width and height
# Thomas Konigkramer
# 29 March 2014

def print_square():
        print("*****\n"
              "*   *\n"
              "*   *\n"
              "*   *\n"
              "*****")
    
def print_rectangle(width,height):
        print(width * "*")
        for i in range(height-2):
                print("*", "*", sep = (width-2) * " ")
        print(width * "*")
    
def get_rectangle(width,height):
        line = "*" * width
        ledge = "*"
        redge = "*"
        emptybox = (width - 2) * " "
        newline = "\n"
        rect = line + newline + (height - 2) * (ledge + emptybox + redge + newline) + line
        return rect