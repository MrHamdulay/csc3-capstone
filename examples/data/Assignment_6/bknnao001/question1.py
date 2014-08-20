#bknnao001
#list of name

nS= []
print ("Enter strings (end with DONE):")
name = ""
longest = 0
while name != 'DONE':
      name = input ("")
      if name != 'DONE':
            nS.append (name)
            if len(name) > longest:
                  longest = len(name)
         #longest=max(names,key=len)
            # newlist="{0:>longest}".format(names)      
print ("\nRight-aligned list:")
for name in nS:
      print (("{:>"+str(longest)+"}").format(name))
