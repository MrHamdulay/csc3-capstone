# Yudhi Moodley
# Assignment 6 - Justification program
# 23/04/2014

array = [] # Created an empty string outside the function
def justifyer():
  maximum_length = 0 # manipulated variable to call alignment
  arrayCounter = 0  # counts the number to spaces required to align
  rope = "" # because string is too generic
  
  print("Enter strings (end with DONE):")
  while rope != 'DONE': # sentinel
          rope = input()
          array.append(rope)
          arrayCounter += 1
          
          
          if len(rope) >= maximum_length: 
              maximum_length = len(rope) # sets the max length of the variable
              
  array.remove('DONE') # can't let it be part of what's to be returned
  arrayCounter = arrayCounter-1


  print('')
  print("Right-aligned list:")
  
  for i in range (arrayCounter):
      difference_spaces = maximum_length - len(array[i]) 
      print(" "*difference_spaces + array[i])

justifyer()