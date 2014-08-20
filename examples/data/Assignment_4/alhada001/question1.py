import boxes

choices = input ("Choose test:\n")
actions = choices[:1]
if actions == 'a':
   boxes.print_square ()
elif actions == 'b':
   width, height = map (int, choices[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (width, height)
   print ("called function")
elif actions == 'c':
   width, height = map (int, choices[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (width, height)
   print ("called function")
   print (figure)