print("Enter a space-separated list of marks:")
names=[] #introducing empty string
name1=""#introducing empty list
name1 = input() #getting input from user
name2=name1.split(" ") #new varible where name1 is split
count_fail=0 #introducing variables...
count_3rd=0
count_lower2nd=0
count_upper2nd=0
count_1st=0
for i in range(len(name2)): #itterate through the length of the list
    if int(name2[i])<50: #add to fail list when people get less than 50
        count_fail+=1
    elif int(name2[i])<60: #add to 3rd list when people get less than 60
        count_3rd+=1
    elif int(name2[i])<70: #add to lower 2nd list when people get less than 70
        count_lower2nd+=1
    elif int(name2[i])<75: #add to upper 2nd list when people get less than 75
        count_upper2nd+=1
    else: #add to 1st list when people get more than 75
        count_1st+=1
#printing results with Xs representing number of students with each result
print('1 |',count_1st*'X',sep='')
print('2+|', count_upper2nd*'X',sep='')
print('2-|',count_lower2nd*'X',sep='')
print('3 |',count_3rd*'X',sep='')
print('F |',count_fail*'X',sep='')