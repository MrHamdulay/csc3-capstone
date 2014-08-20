# test program for box drawer

import boxes

choice = input ("Choose test:\n")
action = choice[:1]
if action == 'a':
   boxes.print_square ()
elif action == 'b':
   w, h = map (int, choice[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (w, h)
   print ("called function")
elif action == 'c':
   w, h = map (int, choice[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (w, h)
   print ("called function")
   print (figure)
      
