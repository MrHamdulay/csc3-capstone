"""Remove repetition
Emmanuel Conradie
02 May 2014"""

#Enter input
print ("Enter strings (end with DONE):")
alist = []
blist = []
while True:
     string = str(input())
     alist.append(string)
     if string == 'DONE':
          alist.remove('DONE')
          break
#remove repitition
print ("\nUnique list:")
for i in alist:
     if not i in blist:
          blist.append(i)
#print list
for j in blist:
     print (j)