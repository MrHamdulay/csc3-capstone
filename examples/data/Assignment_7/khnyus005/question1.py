'''
Created on 01 May 2014
Unique strings
@author: Yusuf Khan
KHNYUS005
'''
vote = ''
candid8s = []#defining variables outside of loop

print("Enter strings (end with DONE):")

while True:#infinite loop
    vote = input()#new input
    if vote == 'DONE':
        break
    if vote not in candid8s:
        candid8s.append(vote)#adds if unique

print("\nUnique list:")#output     
for i in candid8s:
    print (i)