"""Adam Kaliski KLSADA002
CSC1015F Assignment 6 question 3
vote counting"""
print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
s=input()
list={}

while s != 'DONE':
    if s in list:
        list[s]+=1
    else:
        list[s]=1
    s=input()
print('\nVote counts:')
for i in sorted(list):
    print('{:<9} {:>4}'.format(i,('- '+str(list[i]))))