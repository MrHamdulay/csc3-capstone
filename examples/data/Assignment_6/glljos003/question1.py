"""program to allow user to enter a list of strings with sentinel "DONE", then list is printed right aligned with longest string
joshua gullan
22 april 2014"""

x=input("Enter strings (end with DONE):\n")

#create empty list and append names until sentinel "DONE" is typed
people= []

if x=="DONE":
   print("\nRight-aligned list:")

#prints right-aligned list using format
else:
   while x!="DONE":
      people.append(x)
      x=input()
   print("\nRight-aligned list:")
   max_length=(max(people, key=len))
   max_length=len(max_length)
   for i in (people):
      print((max_length-len(i))*" ",i,sep="")

    
    
    

