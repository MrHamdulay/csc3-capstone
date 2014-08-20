height = eval(input("Enter the height of the triangle: \n"))
def pyramid(nrrows):
          for i in range(height):
                    rowformat =[((height-i)-1)*' ' + i*'*' + '*' + i*'*']
                    for j in rowformat:
                              print(j)
pyramid(height)
               
