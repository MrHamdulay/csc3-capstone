'''
Created on 22 Apr 2014
prints right aligned list
@author: Yusuf Khan
KHNYUS005
'''
#defining necessary variables outside of loop
length = 0
names = []#defining array
name = input("Enter strings (end with DONE):\n")

while name != 'DONE':#watch for sentinel
    names.append(name)#append to list
    if len(name) > length:
        length = len(name)#finds longest name
    name = input('')#asks for more input

print()
print("Right-aligned list:")
for i in range(len(names)):#loop through elements in array
    print ('{0:>{length}}'.format(names[i],length=length))
    #formatter string to format output