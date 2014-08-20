# draw an isoceles triangle
# hs
# 16 march 2011

height = eval (input ("Enter the height of the triangle:\n"))
 
   
for i in range (1, height+1, 1):
   spaces = height-i
   for j in range (0, spaces):
      print (" ",end="")
   width = (i*2-1)
   for j in range (0, width):   
      print ("*",end="")
   print() 