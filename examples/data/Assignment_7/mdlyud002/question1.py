# Yudhi Moodley
# Assignment 7 - Repetition omission program
# 29/04/2014

array = [] # Created an empty string outside the function
def omitter():
  arrayCounter = 0  # counts the number of strings
  rope = "" # because string is too generic
  
  print("Enter strings (end with DONE):")
  while rope != 'DONE': # sentinel
          rope = input()

          if rope not in array:
            array.append(rope)
            arrayCounter += 1
         
          else:
            rope= ""
              
              
  array.remove('DONE') # can't let it be part of what's to be returned

  arrayCounter -= 1

  print("\nUnique list:")

  for i in range (arrayCounter):
    print(array[i])

omitter()