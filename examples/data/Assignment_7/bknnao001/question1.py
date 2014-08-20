nS= []
print ("Enter strings (end with DONE):")
name = ""
while name != 'DONE':
      name = input ("")
      if name not in nS:
            nS.append (name)
            #if nS:
             #     nS.sort()
              #    last=nS[-1]
print("Unique list:")
for i in nS:
      print (i)
      
      
      