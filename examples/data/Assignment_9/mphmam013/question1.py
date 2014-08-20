"""Mphuthi Mamorena
assignment 9
question 1"""

filename=input("Enter the marks filename:\n")

f= open(filename,'r')
lines=f.readlines()
f.close()

counter=len(lines)



newlist=[]

for line in lines:
    line=line.split(',')
    newlist.append(line)
    
    
sumall=0
for i in range(len(newlist)):
    sumall+=int(newlist[i][1])
    
import decimal

average=sumall/counter

ave=str(average)
if ave[-1]=='0':
    print("The average is:",ave+'0') 

else:
    print("The average is:",round(average,2))  

sumdeviation=0

for f in range(len(newlist)):
    sumdeviation+=((eval(newlist[f][1])-average)**2)
    
import math   
    
deviation=math.sqrt(sumdeviation/counter)

devi=str(deviation)
if devi[-1]=='0':
        print("The std deviation is:",str(deviation)+'0')    

else:    
    print("The std deviation is:",round(deviation,2))
    
    
for i in range(len(newlist)):
    if eval(newlist[i][1])<average-deviation:
        print("List of students who need to see an advisor:")
        break
for i in range(len(newlist)):
    if eval(newlist[i][1])<average-deviation:

        print(newlist[i][0])




    
    
