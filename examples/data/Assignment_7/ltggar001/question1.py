'''Program to turn all items in a list unique
Gareth Lategan
02-05-2014'''

list=[]

a=input("Enter strings (end with DONE):\n")

while a!="DONE":
    list.append(a)
    a=input()

list.reverse()

for q in range(len(list)):
    if list.count(list[q])>1:
        list[q]='fake'

list.reverse()

print("\nUnique list:")

for i in range(len(list)):
    if list[i]!='fake':
        print(list[i])