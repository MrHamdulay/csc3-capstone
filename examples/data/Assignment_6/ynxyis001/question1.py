#Right-aligns names inserted by user
#Jennifer Yuan
#22 April 2014

names = [] #empty string
aname = input ("Enter strings (end with DONE):\n") #gets names from user
while aname != "DONE": #DONE = sentinel
   names.append (aname) #adds name to list of names
   aname = input ("") #continues loop

r=0   
for i in names: #finds the name with the maximum number of letters
   if len(i) > r:
      r=len(i)
      
print("\nRight-aligned list:")


for i in names:
   print(i.rjust(r)) #right-aligns everything in list according to longest name and prints 
   
   


