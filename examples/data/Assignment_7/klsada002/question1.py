"""stores and prints a list of strings without duplicates
KLSADA002
CSC1015F Assignment 7 Q1
29/04/14"""

A = []
s= input('Enter strings (end with DONE):\n')
while(s != 'DONE'):
    if s not in A:
        A.append(s)
    s = input()
print('\nUnique list:')
for i in A:
    print(i)