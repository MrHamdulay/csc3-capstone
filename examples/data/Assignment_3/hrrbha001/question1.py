# draw a rectangle
# hs
# 16 march 2011

height = eval (input ("Enter the height of the rectangle:\n"))
width = eval (input ("Enter the width of the rectangle:\n"))

for row in range (0, height):
   for col in range (0, width):
      print ("*",end="")
   print ()