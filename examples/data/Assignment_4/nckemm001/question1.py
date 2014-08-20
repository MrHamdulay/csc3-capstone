# Question 1
# Creating hollow boxes of stars using functions

import boxes

choice = input ("Choose test:\n")
action = choice[:1]

if action == 'a':
   boxes.print_square ()
   
elif action == 'b':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (width, height)
   print ("called function")
   
elif action == 'c':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (width, height)
   print ("called function")
   print (figure)
      
