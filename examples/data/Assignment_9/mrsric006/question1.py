import math

filename = input("Enter the marks filename:\n")
f = open (filename,"r")
line = f.readlines()
newlist=[]
namelist=[]
f.close()
for i in line:
   i = i.strip('\n')
   i = i.split(',')
   for j in i:
      if j.isdigit():
         newlist.append(j)
      else:
         namelist.append(j)

sumav = 0        
for num in newlist:
   sumav += eval(num)
   av = sumav/(len(newlist))

print("The average is: "+"{0:.2f}".format(round(av,2)))

sumstd = 0
for i in newlist:
   sqr = (eval(i)-av)**2 
   sumstd += sqr

std = math.sqrt(sumstd/len(newlist))

print("The std deviation is: "+"{0:.2f}".format(round(std,2)))

for i in range(len(newlist)):
   if eval(newlist[i]) < (av-std):
      print("List of students who need to see an advisor:")
      break

for i in range(len(newlist)):
   if eval(newlist[i]) < (av-std):
      print(namelist[i])
