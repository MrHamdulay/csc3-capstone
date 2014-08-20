names = []
print ("Enter strings (end with DONE):")
name = ""
longest = 0
while name != 'DONE':
   name = input ("")
   if name != 'DONE':
      names.append (name)
      if len(name) > longest:
         longest = len(name)
      
print ("\nRight-aligned list:")
for name in names:
   print (("{:>"+str(longest)+"}").format(name))