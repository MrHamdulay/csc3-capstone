# test program for box drawer

import boxes

option = input ("Choose test:\n")
choice = option[:1]
if choice == 'a':
   boxes.print_square ()
elif choice == 'b':
   width, height = map (int, option[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (width, height)
   print ("called function")
elif action == 'c':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (width, height)
   print ("called function")
   print (figure)
      
