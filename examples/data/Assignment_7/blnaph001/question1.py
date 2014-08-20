#unique list
#aphiwe baleni
#29 april 2014
list=[]
print('Enter strings (end with DONE):')
while True:
    word=input('')
    if word=='DONE':
        break
    counter=list.count(word)
    if counter==0:
        list.append(word)
    if counter>1:
        continue
print()
print('Unique list:')
for name in list:
    print(name)