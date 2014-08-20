# test program for Ndom calculations
"""
Prashanth Sridharan
SRDPRA001
Assignment 4
question 2
"""
import ndom

chc = input ("Choose test:\n")
act = chc[:1]
print ("calling function")
if act == 'n' or act == 'd':
   no = int(chc[2:])
   if act == 'n':
      answer = ndom.ndom_to_decimal (no)
   else:
      answer = ndom.decimal_to_ndom(no)
elif act == 'a' or act == 'm':
   no1, no2 = map (int, chc[2:].split(" "))
   if act == 'a':
      answer = ndom.ndom_add (no1, no2)
   else:
      answer = ndom.ndom_multiply (no1, no2)
print ("called function")
print (answer)
