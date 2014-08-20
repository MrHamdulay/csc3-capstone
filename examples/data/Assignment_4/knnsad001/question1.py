# test program for box drawer

import boxes

choice = input ("Choose test:\n")
action = choice[:1]
if action == 'c':
   boxes.print_square ()
elif action == 'd':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (width, height)
   print ("called function")
elif action == 'e':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (width, height)
   print ("called function")
   print (figure)
      
