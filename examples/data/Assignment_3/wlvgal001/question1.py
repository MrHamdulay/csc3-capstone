#question 1

def rectangle(star):
    x=eval(input("Enter the height of the rectangle:\n"))
    y=eval(input("Enter the width of the rectangle:\n"))
    for i in range(x):
        print(star*y)

rectangle("*")
        
        
        