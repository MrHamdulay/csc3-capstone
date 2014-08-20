#Assignment 3
#Question 2 

def triangle():
    height = eval(input("Enter the height of the triangle: \n"))
    i = 1
    c = height
    while i < height + 1:
        w = 2*i - 1
        print(' '*(c-1),'*'*w, sep='')
        i +=1
        c -=1
    
    
triangle()