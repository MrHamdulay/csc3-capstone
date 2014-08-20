"""Mokoena Mafologele
02/05/2014
"""
#Create empty list
u_list=[]
strings=input("Enter strings (end with DONE):\n")
while strings.lower()!="done":
    if strings not in u_list:
        u_list.append(strings)
    strings=input()
print("\nUnique list:")
for i in u_list:
    print(i)
