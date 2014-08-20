h=eval(input("Enter the height of the rectangle:\n")) #This Programme makes a rectangle of stars after your inputs
w=eval(input("Enter the width of the rectangle:\n"))
for i in range(h): #If your i is equal to your height it breaks so your shape is perfect
    print("*"*w)
    i=1+1
    if i==h:
        break