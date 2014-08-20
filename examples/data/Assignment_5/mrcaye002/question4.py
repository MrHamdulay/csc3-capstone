"""Program to draw a text-based graph of a mathematical function f(x)
Ayesha Marcus
15/04/2014"""

import math


def question4(equation):
  
  character = ""
  #going down
  for y in range(10,-11,-1):
    str=""
    #going to the right
    for x in range(-10,11):
      character = " "
      
      #Y Axis
      if y == 0:
        character = "-"
      
      #X Axis
      if x == 0:
        character = "|"

      #X-Y Centre [cross hair]
      if x == 0 and y == 0:
        character = "+"
        
      if round(eval(equation),0) == y:
        character = "o"
 
    #  print (character, end="")
    #print ()
      str=str+character
    print (str)
    #print (str) 
    #print (str," ", strVal, "[x] ",xVal,"[y] ", yVal)

  return;


def main ():
   
   fx=input("Enter a function f(x):\n")
   question4 (fx)

if __name__ == "__main__":
   main()
