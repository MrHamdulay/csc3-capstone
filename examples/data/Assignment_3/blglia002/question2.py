tri= eval(input("Enter the height of the triangle: \n"))
gap=tri-1
for i in range(1,tri+gap+2,2):
          print(gap*" ",i*"*",sep='')
          gap=gap-1
          
    
