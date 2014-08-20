#for the square
def print_square():
        print("*****")
        print("*   *")
        print("*   *")
        print("*   *")
        print("*****")

#for the rectangle
def print_rectangle(width,height):
        
        space = " "
        
        t = width -2
        spaces = space*t
        row1 = "*"*width
        print(row1)
        row2 = "*"
        
        for i in range (height-2):
                print(row2+spaces+row2)
        print("*"*width)
        

def get_rectangle(width,height):
        spaces = ' '
        t = width -2 
        spaces = spaces*t
        row1 = "*"*width
        figure = row1 + "\n"
        row2 = "*"
        for i in range (height -2):
                figure = figure + row2 + spaces + row2 + "\n"
        figure = figure+"*"*width
        
        return figure

#get part?
