#Mufaro Chiwara - 27 April 2014
# Get Input

lis = input("Enter strings (end with DONE):\n")
words =[]
while lis!='DONE':
    words.append(lis)
    lis = input()
print()
print('Unique list:')
newwords=[]
#Find repeats
for i in words:
    if i not in newwords:
        newwords.append(i)
        print(i)
        


