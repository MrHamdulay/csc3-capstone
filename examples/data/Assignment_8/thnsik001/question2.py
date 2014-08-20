""" Assignment 8 
Question2 - pairs of characters
THNSIK001"""

def pairs(strin):
  """counts iterations"""
  if strin =="" or len(strin)== 1:
    return 0
  elif strin[0] == strin[1]:
    strin = strin[2:]
    return 1 + pairs(strin)    
  else:
    strin = strin[1:]
    return pairs(strin[1:]) 
  
strin = (input("Enter a message:\n"))
pair_s = (pairs(strin))
print("Number of pairs:",pair_s)