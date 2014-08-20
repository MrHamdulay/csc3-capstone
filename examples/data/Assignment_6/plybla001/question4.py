"""Sort marks into categories
B.Player
20/04/2014"""

#Capture data
marks = input("Enter a space-separated list of marks:\n").split()
for i in range(len(marks)):
   marks[i]=eval(marks[i])

#count
count={'1':0,'2+':0,'2-':0,'3':0,'F':0}
for mark in marks:
   if mark >= 75:  count['1']+=1    
   elif mark >= 70: count['2+']+=1
   elif mark >= 60: count['2-']+=1 
   elif mark >= 50: count['3']+=1 
   else: count['F']+=1
   
#output results
print("1 |","X"*count['1'],sep='')
print("2+|","X"*count['2+'],sep='')
print("2-|","X"*count['2-'],sep='')
print("3 |","X"*count['3'],sep='')
print("F |","X"*count['F'],sep='')

