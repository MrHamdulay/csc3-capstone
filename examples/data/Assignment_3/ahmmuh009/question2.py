#q2 for ass3
#ahmmuh009




def triangle(p,w=0):
       for i in range(p):
              print ((' ' * (p-1)) + ("*" * (w*2+1)))
        
              return triangle(p-1, w+1)

p=eval(input("Enter the height of the triangle:\n"))
triangle (p)