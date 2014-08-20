#Thembekile Dubazana
#dbzphi002
#Assignment 6:Q3

"""Histogram of UCT Marks"""

#The input and variables
marks=input("Enter a space-separated list of marks:\n")
mark=marks.split()
count=0
count1=0
count2=0
count3=0
count4=0
category={}
Class=['first','u2nd','l2nd','third','fail']

#Loop through list to get dictionary
for i in mark:
    if int(i) >= 75:
        count+=1
        category[Class[0]]=count
    elif int(i) >= 70:
        count1+=1
        category[Class[1]]=count1
    elif int(i) >= 60:
        count2+=1
        category[Class[2]]=count2
    elif int(i) >= 50:
        count3+=1
        category[Class[3]]=count3
    else:
        count4+=1
        category[Class[4]]=count4        
for i in range(len(Class)):
    if Class[i] not in category:
        category[Class[i]]=0

print("1 |","X"*category['first'],sep="")
print("2+|","X"*category['u2nd'],sep="")
print("2-|","X"*category['l2nd'],sep="")
print("3 |","X"*category['third'],sep="")
print("F |","X"*category['fail'],sep="")


    
    

