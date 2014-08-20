#Program to do basic vector calculations in 3 dimensions
#Ayesha Marcus
#22/04/2014

import math

def fAdd(v1, v2):                       #Addition
  tmp = []                              #Empty list
  for i in range(len(v1)): 
    tmp.append(int(v1[i]) + int(v2[i])) # Calculate A+B and add to list
  print('A+B =',tmp)
  return

def main ():                    
  vecA = []
  vecB = []
  print ("Enter vector A:")           #Ask user for input
  sIn = input("")
  vecA = sIn.split(' ')               #Split string into list

  print ("Enter vector B:")           #Ask user for input
  sIn = input("")
  vecB = sIn.split(' ')               #Split string into list by space delimeter

  fAdd(vecA, vecB)                   
  fMultiply(vecA, vecB)               
  fSquare(vecA, 'A')
  fSquare(vecB, 'B')


def fMultiply(v1, v2):               #function to multiply
  tmp = []
  for i in range(len(v1)):             
    tmp.append(int(v1[i]) * int(v2[i])) #Add the product to the list
  
  total = 0
  for i in range(len(tmp)):
    total = total + tmp[i]
  print('A.B =',total)
  return

def fSquare(v1, label):
  txt = '|' + label + '|'
  tmp = []
  for i in range(len(v1)):
    tmp.append(pow(int(v1[i]),2))
  
  total = 0
  for i in range(len(tmp)):
    total = total + tmp[i]
  print(txt,'=',"%0.2f" % round(math.sqrt(total),2))
  return


    

if __name__ == "__main__":
   main()
