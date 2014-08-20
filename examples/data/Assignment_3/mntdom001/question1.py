# question1.py
# Author: Dominic Manthoko
# 22 March 2014

def rect():
    # get input from the user. First get the height of the rectangle and then
    #    the width of the rectangle
    height = eval(input("Enter the height of the rectangle: \n"))   
    width = eval(input("Enter the width of the rectangle: \n"))
    
    print(("*"*width + '\n') * height)
    
if __name__ == '__main__':
    rect()
    