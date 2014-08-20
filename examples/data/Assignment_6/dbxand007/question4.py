"""Cherise Dube
19 April 2014
Program to draw a histogram of a list of marks"""

marks=input("Enter a space-separated list of marks:\n").split(" ")

#Counts how many individuals have achieved certain marks
count_fail=0
count_3rd=0
count_lower2nd=0
count_upper2nd=0
count_1st=0
counters=[]
for i in marks:
    ind_mark=eval(i)
    if ind_mark<50:
        count_fail+=1
        
    elif 50<=ind_mark<60:
        count_3rd+=1
        
    elif 60<=ind_mark<70:
        count_lower2nd+=1
    
    elif 70<=ind_mark<75:
        count_upper2nd+=1
        
    else:
        count_1st+=1
        
#Creates a ist of the counters
counters.append(count_1st)
counters.append(count_upper2nd)
counters.append(count_lower2nd)
counters.append(count_3rd)
counters.append(count_fail)

print("1 |","X"*counters[0],sep="")
print("2+|","X"*counters[1],sep="")
print("2-|","X"*counters[2],sep="")
print("3 |","X"*counters[3],sep="")
print("F |","X"*counters[4],sep="")



        


