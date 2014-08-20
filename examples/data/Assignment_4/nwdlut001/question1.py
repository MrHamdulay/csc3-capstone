import boxes
def main():
    y=input("Choose a test:\n")
    z=y[:1]
    if z=='a':
        boxes.print_square()
    elif z=='b':
        boxes.print_rectangle(width,height)
    elif z=='c':
        width1, height1 = map (int, choice[2:].split(" "))
        print ("calling function")
        figure = boxes.get_rectangle (width1, height1)
        print ("called function")
        print (figure)        
main()