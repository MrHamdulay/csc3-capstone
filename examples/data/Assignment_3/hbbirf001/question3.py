'''
Created on 23 Mar 2014

@author: Yusuf
'''
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
length = len(message)

for i in range(thickness):
    print(i*'|'+'+'+(length+(2*thickness)-2*i)*'-'+'+'+i*'|')

for r in range (repeat):
    print(thickness*'|'+' '+message+' '+thickness*'|')
    
for i in range(thickness-1,-1,-1):
    print(i*'|'+'+'+(length+(2*thickness)-2*i)*'-'+'+'+i*'|')