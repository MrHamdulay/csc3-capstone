#Lauren de Bruyn
#Program to print a right-aligned list of names
#22 April 2014

#get list of names from the user
names = []
aname = input ("Enter strings (end with DONE):\n")
while aname != "DONE":
   names.append (aname)
   aname = input ("")

#determine maximum length of name
#maxlen=0
for i in names:
   maximum = max(names, key=len)
   new_maximum = len(maximum)    
   #if len(i)>maxlen:
      #maxlen=len(i)

#print list of names right justified
print("\nRight-aligned list:")
for name in names:
   print(" "*(int(new_maximum)-len(name)),name,sep='')