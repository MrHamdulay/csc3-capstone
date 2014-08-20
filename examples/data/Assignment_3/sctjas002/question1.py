height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))
def sq(H):
    for i in range(H):
        print("*"*width)

def sq2(H):
    print(("*"*height+'\n')*height)

if __name__=='__main__':
    sq(height)
    