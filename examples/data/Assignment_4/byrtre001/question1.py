# test program for box drawer
import boxes
choice=input('Choose test:''\n')
action = choice[:1]
if action == 'a':
   boxes.square(5)
elif action == 'b':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   boxes.rectangle(width,height)
   print ("called function")
elif action == 'c':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   print ("called function")
   boxes.rectangle(width,height)
      
