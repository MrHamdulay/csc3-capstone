# test program for box drawer

import boxes

c = input ("Choose test:\n")
a = c[:1]
if a == 'a':
   boxes.print_square ()
elif a == 'b':
   w, h = map (int, c[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (w, h)
   print ("called function")
elif a == 'c':
   w, h = map (int, c[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (w, h)
   print ("called function")
   print (figure)
      
