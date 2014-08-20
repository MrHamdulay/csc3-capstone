# Module containing functions for creating boxes
# Nevarr Pillay - PLLNEV006
# 29 March 2014

def print_square():
    for i in range(5):
        if i == 0 or i == 4:        
            for j in range(5):
                print("*",end="")                
        else:
            for j in range(5):
                if j == 0 or j == 4:
                    print("*",end="")
                else:
                    print(" ",end="")
        print()
        
def print_rectangle(width,height):
    for i in range(height):
        if i == 0 or i == height-1:        
            for j in range(width):
                print("*",end="")                
        else:
            for j in range(width):
                if j == 0 or j == width-1:
                    print("*",end="")
                else:
                    print(" ",end="")
        print()    
            
def get_rectangle(width,height):
    rect = ""
    for i in range(height):
        if i == 0 or i == height-1:        
            for j in range(width):
                rect += "*"                
        else:
            for j in range(width):
                if j == 0 or j == width-1:
                    rect += "*"
                else:
                    rect += " "
        rect += "\n"
    return rect   
                