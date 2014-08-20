"""Adam Kaliski KLSADA002
CSC1015F Assignment 6 Question 1
Right justifies list of strings"""

s = input('Enter strings (end with DONE):\n')
listy = []
leng = 0
count=0
while s != 'DONE':
    listy.append(s)
    if len(s)>leng:
        leng = len(s)
    count+=1
    s=input('')
print('\nRight-aligned list:')
for i in range(0,len(listy)):
    print (listy[i].rjust(leng))
    