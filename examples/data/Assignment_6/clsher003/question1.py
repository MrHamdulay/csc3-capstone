"""program to print a list of names right-aligned
herman claassens
20 april 2014"""

names=[]
lengths=[]
name = input ("Enter strings (end with DONE):\n") #get names
while name != "DONE": #sentinel to stop loop
   names.append (name) #add length of names and names to 2 empty lists
   lengths.append(len(name))
   name = input ("")
lengths.sort()  #determine longest name
lengths.reverse()
print()
if lengths==[]:
   print("Right-aligned list:")
else:
   longest_string=lengths[0]
   print('Right-aligned list:')
   for name in names:
      length_name=len(name)   
      spaces=longest_string-length_name 
      print(' '*spaces+name) # print spaces and name
   
   