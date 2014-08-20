"""question three of assignment 6"""

print("Independent Electoral Commission\n--------------------------------")

names =[]

name = input ("Enter the names of parties (terminated by DONE):\n")

while name !='DONE':
    names.append(name)
    name=input()
    
print()
print("Vote counts:")
names = sorted(names)


for x in sorted(set(names)):
  
    
    
    print ("{0:11}- {1}".format( x, names.count(x) ) )
    
    
    #print ("{0:11}- {1}".format( x, a ) )

  
