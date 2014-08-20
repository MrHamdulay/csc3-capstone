"""Program that takes in a list of marks and outputs a histogram representation 
   of thr marks
   Bridgette Lefatsa
   LFTNTO002
   24 April  2014"""

#input marks from user
marks=input("Enter a space-separated list of marks:\n")

#marks in array
mark_list=[]
for mark in marks.split(" "):
    mark_list.append(eval(mark))

#catergorise marks
#>=75
count=0
for x in mark_list:
    if x>=75:
        count+=1
print("1 |","X"*count,sep="")

#>=70 and <75
count=0
for x in mark_list:
    if (x>=70) and (x<75):
        count+=1
print("2+|","X"*count,sep="")

#>=60 and <70
count=0
for x in mark_list:
    if (x>=60) and (x<70):
        count+=1
print("2-|","X"*count,sep="")

#>=50 and <60
count=0
for x in mark_list:
    if (x>=50) and (x<60):
        count+=1
print("3 |","X"*count,sep="")

#50
count=0
for x in mark_list:
    if x<50:
        count+=1
print("F |","X"*count,sep="")