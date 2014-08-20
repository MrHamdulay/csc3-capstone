import math                                     
f = input('Enter the marks filename:\n')
infile = open(f, 'r')                  
lines = infile.readlines ()
marks = []
infile.close ()

for line in lines:                  
   student, mark = line.split(',')
   result = mark
   marks.append(int(result))       
sum1=0
for i in marks:                     
   sum1+=i
   
ave=sum1/len(marks)                
d=0
for mark in range(len(marks)):
   d+=((marks[mark]-ave)**2)
   
std =d/len(marks)
   
standev = math.sqrt(std)     
   
print('The average is: {0:.2f}'.format(ave))

print('The std deviation is: {0:.2f}'.format(standev))

for i in range(len(marks)):
   
   if float(int(marks[i]))<(ave-standev):
       print('List of students who need to see an advisor:')
       break


for i in range(len(marks)): 
       
   if float(int(marks[i]))<(ave-standev):
      x,y=lines[i].split(",")
      print(x)










