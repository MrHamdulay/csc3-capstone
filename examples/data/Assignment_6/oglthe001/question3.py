"""counting votes
theresa ogallo 2014"""

print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')

#getting a list of parties
x=[]
n=''
while n != 'DONE':
    n=input('')
    x.append(n)
    
x.remove('DONE')

print()
print('Vote counts:')

#counting the votes, sorting and printing out the parties and votes
x.sort()
    
new_x=set([y for y in x if x.count(y) > 1])

for j in x:
    votes=str(x.count(j))

for y in new_x:
    format_new_x='{0:11}'.format(y)
    print(format_new_x+'-',votes)