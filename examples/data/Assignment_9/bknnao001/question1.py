#14/05/2014
#BKNNAO001
#def filename():
#s=standard deviation;c=compte
import math
filename=input("Enter the marks filename:\n")
f=open(filename,"r")
d=f.readlines()
f.close ()
a=0
c=0
for i in d:
   i=i[:-1]
   fld=i.split(",")
   if len(fld)== 2:
      c+=1
      a+=int(fld[1])
mean=a/c
print ("The average is: {:.2f}".format (mean))
s=0
for i in d:
   i=i[:-1]
   fld=i.split (",")   #fld=fields
   if len(fld)==2:
      s+= (int(fld[1])-mean)**2
s= math.sqrt(s/c)      
print ("The std deviation is: {:.2f}".format(s))
e=0
for i in d:
   i=i[:-1]
   fld=i.split(",")
   if len(fld) == 2:
      if int(fld[1])<(mean-s):
         if e==0:
            e=1
            print("List of students who need to see an advisor:")
         print(fld[0])
