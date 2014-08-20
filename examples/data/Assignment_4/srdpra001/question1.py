# test program for box drawer
"""
Prashanth Sridharan
SRDPRA001
Assignment 4
Question 01
"""
import boxes

chc = input ("Choose test:\n")
act = chc[:1]
if act == 'a':
   boxes.print_square ()
elif act == 'b':
   wth, ht = map (int, chc[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (wth, ht)
   print ("called function")
elif act == 'c':
   wth, ht = map (int, chc[2:].split(" "))
   print ("calling function")
   fig = boxes.get_rectangle (wth, ht)
   print ("called function")
   print (fig)
      
