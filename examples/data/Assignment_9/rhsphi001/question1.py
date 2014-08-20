'''Phillip Ruhesi
15/05/2014
program to open a file and calculate mean standard deviation return list of students got less than one standard deviation below the mean'''

import math
fname=input('Enter the marks filename:\n')                                      
infile = open(fname,"r")                                   #open file to be read
array=[]
reada = infile.readline()                               #read first line of file
reada=reada[0:-1]
array.append(reada.split(','))
while reada!='':
  reada=infile.readline()
  reada=reada[0:-1]
  array.append(reada.split(','))
infile.close()                                                   #close the file

array.remove(array[-1])

Names=[]
Marks=[]
for i in array:
  Names.append(i[0])
  Marks.append(i[1])
Marks=list(map(eval, Marks)) #change all values in Marks from string to integers
Average=sum(Marks)/len(Marks)
#calculate standard deviation
def standarddev():
  total=0
  for i in range(len(Marks)):
    total+=(Marks[i]-Average)**2         
  Sdev=math.sqrt(total/len(Marks))  
  return Sdev

print('The average is:',end=' ')
print("{0:.2f}".format(Average))
print('The std deviation is:',"{0:.2f}".format(round(standarddev(),2))) #format the output to 2 decimal places
for i in range(len(Marks)):
  if Marks[i]<(Average-standarddev()):
    print('List of students who need to see an advisor:')
    break

for i in range(len(Marks)):
  if Marks[i]<(Average-standarddev()):
    print(Names[i])
    