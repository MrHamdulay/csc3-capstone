#Emile McLennan
#27/4/14
#A7 Q1

strArr=[]
strs=input('Enter strings (end with DONE):\n')
strArr.append(strs)
count=0
num=0
while strs !='DONE':
    if strs in strArr: #see if item is unique
        num+=1
    else:
        strArr.append(strs) #if unique, add to list
        count+=1
    strs=input('')
print()
print('Unique list:') #iterate over the list
for i in range(count+1):
    if strArr[0] !='DONE':
        print(strArr[i])