# question1.py 
#   a program to draw an isoceles triangle of a given height.

def main():
    height=eval(input("Enter the height of the triangle:\n")) 
    space=height-1
    for i in range(height):
        print(((space)*(" "))+(i+(i+1))*("*"))
        space=space-1
        
main() 