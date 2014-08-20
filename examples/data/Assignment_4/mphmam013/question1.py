import boxes
def main():
    x=input("Choose a test:\n")
    v=x[:1]
    if v=='a':
        boxes.print_square()
    elif v=='b':
        boxes.print_rectangle(width,height)
    elif v=='c':
        width, height = map (int, choice[2:].split(" "))
        print ("calling function")
        figure = boxes.get_rectangle (width, height)
        print ("called function")
        print (figure)        
main()