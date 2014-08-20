# Assignment 7
# Question 1
# Richard van Gysen
# 29 April 2014
# Enter strings
strings = input("Enter strings (end with DONE):\n")
lis = []
# Add strings
if strings!='DONE':
    lis.append(strings)
# Terminate list when DONE is entered
while strings!='DONE':
    strings = input()
    if strings =='DONE':
        break    
    else:
        lis.append(strings)
new_lis = []
for i in range(len(lis)):
    if  not lis[i] in new_lis:
        new_lis.append(lis[i])
    else:
        pass
               
#print unique list
print()
print("Unique list:")
for item in new_lis:
    print(item)