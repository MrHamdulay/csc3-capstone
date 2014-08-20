"""Right aligning
Emmanuel Conradie
25 April 2014"""

#enter strings
print ("Enter strings (end with DONE):")  
string = input()
slist = []
slist2 = []
while string != 'DONE':
     slist.append (string)
     string = input()
          

for j in range(len(slist)):
     slist2.append(len(slist[j]))
     
a = 0
c = 0
while a<len(slist2):
     if slist2[a] > c:
          c = slist2[a]
     
     a += 1
#align strings
print ("\nRight-aligned list:")
d = 0
while d < len(slist):
     print (" "*(c - (slist2[d])), slist[d], sep = "")
     d += 1
