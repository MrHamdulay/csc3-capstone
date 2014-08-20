from math import sqrt
filename=input('Enter the marks filename:\n')
f=open(str(filename),'r')
lines=f.readlines()
f.close()


if filename:
    
    for i in range (len (lines)):
        if lines[i][-1]=='\n':
            lines[i] = lines[i][:-1]
        
        
counter={}

for item in range (len (lines)):
    if not item in counter:
        #getting the string excluding the mark and comma and making it the key
        #and getting the mark and making it the item in the key.
        x=lines[item][:-3]
        counter[x]=int(lines[item][-2:])
total=0
for value in counter:
    total=total+counter[value]
    ave=total/len(counter)
if total%len(counter)==0:
    print('The average is:', str(int(ave))+'.00')
else:
    print('The average is:', round(ave,2))
variance=0    
for value in counter:
    variance=variance+((counter[value]-ave)**2)
stdev=sqrt(variance/len(counter))

if stdev-int(stdev)==0:
    print('The std deviation is:', str(int(stdev))+'.00')
else:
    print('The std deviation is:', round(stdev,2))

for value in counter:
    if counter[value]<(ave-stdev):
        print('List of students who need to see an advisor:\n'+value)
    
    
    
         
 
        
    
  
        