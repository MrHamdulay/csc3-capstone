"""a program to right-align list according to longest string
Sarayn Subroyen
21 april 2014"""

#enter and print list strings(names)

names = []
name = input ("Enter strings (end with DONE):\n") #DONE is a sentinel
maximum=0
while name != "DONE":
   names.append (name)
   length=len(name)
   name = input ("")
   if length>maximum:   #find longest string
      maximum=length
print() 
   
#print right-aligned
print("Right-aligned list:")

for name in names:
   print((maximum-(len(name)))*" "+name)
 
