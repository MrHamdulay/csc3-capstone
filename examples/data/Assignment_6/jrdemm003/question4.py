"""assignment 6, Q4... histogram of marks
emma jordi
22 april 2014"""

#set empty list for all categories
list1=[]
list2plus=[]
list2=[]
list3=[]
listF=[]
#get input
marks=input("Enter a space-separated list of marks:\n")
#split input at empty space
marks=marks.split()

#classify marks
for mark in marks:
    mark = eval(mark)
    if mark >= 75:
        list1.append(mark)
        
    elif 75 > mark >= 70:
        list2plus.append(mark)
        
    elif 70 > mark >= 60:
        list2.append(mark)
    elif 60 > mark >= 50:
        list3.append(mark)
    else:
        listF.append(mark)

#print output
print("1 |","X"*len(list1), sep="")
print("2+|","X"*len(list2plus), sep="")
print("2-|","X"*len(list2), sep="")
print("3 |","X"*len(list3), sep="")
print("F |","X"*len(listF), sep="")