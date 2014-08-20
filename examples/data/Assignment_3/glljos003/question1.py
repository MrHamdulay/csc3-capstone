
def draw(a,b):
    rectangle = "*"*b
    for i in range(a):
        print(rectangle)
    

def main():
    height = eval(input("Enter the height of the rectangle:\n"))
    width = eval(input("Enter the width of the rectangle:\n"))
    draw(height,width)

main()