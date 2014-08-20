""" drawing graphs that the user enters
Ednecia Matlapeng
15 April 2014 Assignment 5"""

import math
yinc = 2/10
xinc=2/10
f = input("Enter a function f(x):\n")
#Separate the function into three puts

#print(slope,power,y_int,sep='\n')
#print the axis first


def graph(x):
   slope = '1'
   power=1
   if f.find('x')<0:
            return int(f)   
   #find gradient
   position = f.find('x')
   if position >0:
      slope =(f[0:position])
   
   y_int=0
   #find power
   if f.find('**')>0:
      position = f.find('**')+1
      power =int(f[(position+1):position+2])
   #Finding y intercept
   y_int=0

   if not( f[-1]=='x' or f[-1]==')'):
      for k in range(len(f)-1,position,-1):
         if f[k].isdigit():
            y_int= (f[k])
         else: break
   y_int= int(y_int)
   
   
   #Breaking down the graph
   #print(slope)
   if (slope).find('s')>=0 or (slope).find('t')>=0:
      #the sine value
      if  slope.find('i')>=0 :
         n_slope = int(slope[:slope.find('s')])
         return n_slope*math.sin(x)**power+y_int
      elif  slope.find('c')>=0 :
            n_slope = int(slope[:slope.find('c')])
            return n_slope*math.cos(x)**power+y_int 
      elif  slope.find('t')>=0 :
            n_slope = int(slope[:slope.find('t')])
            return n_slope*math.tan(x)**power+y_int
      
   else:
      #slope = (slope)
      
      return int(slope)*x**power + y_int
   
#print(graph(4))    
yinc = 2/10     
for y in range(-10,11):
   for x in range(-10,11):
      x_real = x
      y_real = -y      
      #origin
      if y_real-yinc <= graph(x) <= y_real+yinc:
               # print('2323')
            print ("o",end="")      
      elif x_real==0 and y_real==0:
         print ("+",end="")       
       
      elif x_real == 0:
         print ("|",end="")
      elif y_real== 0:
         print ("-",end="")
      else:
         print (" ",end="")
     
        
      #the intercepts
       
   print()
     