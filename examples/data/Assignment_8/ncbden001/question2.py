'''Program to count double letters
   Denzel Ncube
   3 May 2014'''

#Functon to remove last character from a string
def Removelast(string):
  lst = list(string)
  del lst[-1]
  newstring = "".join(lst)
  return newstring

#Function to remove last two characters from a string
def RemoveTwo (string):
  lst = list(string)
  del lst[-1]
  del lst[-1]
  newstring = "".join(lst)
  return newstring  

#Function to get the number of doubles in a variable

def Doubles(string):
  count = 0
  #Turning any input into string
  allstring = str(string)
  #Base case (1 is there to avoid index errors and zero for if the string starts with a double)
  if len(allstring)== 1 or len(allstring)==0 :
    return count
  else:
    #Comparing letters next to each other, incrementing count if they are the same, removing the last character or two characters and the recursive step
    if allstring[-1] != allstring[-2]:
      return count + Doubles(Removelast(allstring))
    elif allstring[-1] == allstring[-2]:
      count += 1
      return count + Doubles(RemoveTwo(allstring))

#Getting input and displaying output
inputstring =input('Enter a message:\n')
print("Number of pairs:" + ' ' +str(Doubles(inputstring)))
    