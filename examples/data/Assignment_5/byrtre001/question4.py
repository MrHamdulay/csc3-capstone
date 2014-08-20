""" draw graphs
Trevor Byaruhanga
18 April 2014"""
# import a function that will enable me to use round 
    
import math
    #prompt the user for an amount
enterfunction=input('Enter a function f(x):'+'\n')
#draw the x and y axes 
for y in range (10,-11,-1):
   
   for x in range (-10, 11):
     # draw the graph if the conditions are met 
      if y==round(eval(enterfunction)):
         print ("o",end="")
      elif x== 0 and y==0:
         print ("+",end="")      
      elif y== 0:
         print ("-",end="")
      elif x== 0:
         print ("|",end="")
      #if the conditions are not met then simply print a spa
      else:
         print (" ",end="")   
         got_x = False   
   
   print ()



