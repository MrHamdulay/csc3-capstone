# program to get list of strings for users and print right-aligned to longest string
# romelon chetty( chtrom001)
# 20 april 2014

#using a sentinal loop to promprt users for list of string
strings=[]
strings.append(input('Enter strings (end with DONE):\n'))
while strings[-1]!='DONE':
    strings.append(input())
    
print()
print('Right-aligned list:')

maxlength=0
for i in strings[:len(strings) - 1]:
    if maxlength<len(i):
        maxlength = len(i)
for j in strings[:len(strings) - 1]:
    print(' '*(maxlength-len(j))+j)


    


    
