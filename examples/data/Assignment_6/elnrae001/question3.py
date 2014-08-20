'''Program to count votes for each political party
Author:Raees Eland
Date:20 April 2014'''

print('Independent Electoral Commission')
print('--------------------------------')

list=[]
print('Enter the names of parties (terminated by DONE):')
string=input() # allows user to input parties
list.append(string)
while string!='DONE':
    string=input()
    list.append(string)
list.remove("DONE")#removes the string 'DONE' at the end of the list

# Creates a list where each party is shown once and tallies up the votes each party recieves
list.sort()
tally=''
for i in list:
    if list.count(i)>=1:
        tally+=str(list.count(i))+' '
        while list.count(i)>1:
            list.remove(i)
tally=tally.split(' ')
print()
print('Vote counts:')
x=0
for j in list:
    s='{0:<10} {1:} {2:}'
    print(s.format(j,'-',tally[x]))
    x+=1
    