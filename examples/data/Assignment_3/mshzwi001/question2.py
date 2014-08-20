# a program to draw an isoceles triangle of a given height using the ‘*’ character. 
# mashau zwivhuya
# 21 march 2014
def main():
    height=eval(input("Enter the height of the triangle:\n"))
    count=1
    gap=height-1
    for i in range(height):
        print(" "*gap,"*"*count,"*"*i,sep="")
        gap=gap-1
        count=count+1
main()        
    
