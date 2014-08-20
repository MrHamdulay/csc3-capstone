""""program to print a list of strings without duplicates
theresa ogallo 2014"""

print('Enter strings (end with DONE):')

#input a list of strings
list1=[]
n=''
while n != 'DONE':
    n=input('')
    list1.append(n)

print()
list1.remove('DONE')

#print a list of strings without dupicates
print('Unique list:')
new_x=list(set([y for y in list1 if list1.count(y) >= 1]))
new_x.sort(key=list1.index)
for i in new_x:
    print (i)