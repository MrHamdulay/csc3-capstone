def print_square():
    print("*" * 5)
    for i in range(3):
        print("*" + "   " +"*")
    
    print("*" * 5)


def print_rectangle(width, height):
    star = "*"
    fullLine = "*" * width
    middle = height - 2
    
    if(width > 0 and height > 0):
        
        print(fullLine)
        
        for i in range(middle):
            if(width == 1):
                print(star)
            elif(width > 1):
                print(star + " " * (width - 2) + star)
                
        if(height > 1):
            print(fullLine)
        

def get_rectangle(width, height):
    star = "*"
    fullLine = "*" * width
    middle = height - 2
    lines = []
    if(width > 0 and height > 0):
        
        lines.append(fullLine)
        
        for i in range(middle):
            if(width == 1):
                lines.append(star)
            elif(width > 1):
                lines.append(star + " " * (width - 2) + star)
                
        if(height > 1):
            lines.append(fullLine)
    return '\n'.join(lines)
