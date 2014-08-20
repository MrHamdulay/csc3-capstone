#A program to draw an isosceles triangle
#Alison Hoernle
#HRNALI002
#19 March 2014

def tri(height):
        j = 1
        k = 1
        while k<= height:
                print(' '*(height-k), "*"*j, sep = '')
                j+=2
                k+=1

if __name__=='__main__':
        height =eval((input("Enter the height of the triangle:\n")))
        tri(height)
        