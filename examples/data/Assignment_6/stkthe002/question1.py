#Thea Sitek, STKTHE002
#10.05.2014
#Print Right-alignes list

#Define list
names = []
length = 1

#add input
adds = input('Enter strings (end with DONE): \n')
while adds != 'DONE':
    names.append(adds)
    adds = input()

for i in names:
    if len(i) > length:
        length = len(i)

#based on length og longest item, right align all list elements    
print('\nRight-aligned list:')
if len(names)>= 1:
    for i in names:
        space = length - len(i)
        print(' '*space, i, sep = '')
        