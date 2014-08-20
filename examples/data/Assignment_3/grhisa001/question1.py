def main():
    h = eval(input("Enter the height of the rectangle:\n"))
    w = eval(input("Enter the width of the rectangle:\n"))
    x=0
    while x<h:
        x+=1
        print(w*'*')
        
main()