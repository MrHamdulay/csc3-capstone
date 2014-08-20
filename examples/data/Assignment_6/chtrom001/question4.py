# counting the number of marks that satisfy the conditions of each category
#romelon chetty
#23 april 2014
#question 4.py

marks=input('Enter a space-separated list of marks:\n') # getting list of marks from user
listmark= marks.split() # putting each mark in a array
listmark.sort()

fir=[]
secup=[]
seclow=[]
third=[]
F=[]

for i in listmark:
        if 75<=int(i)<=100:
                fir.append(i)
        elif 70 <= int(i)< 75:
                secup.append(i)
        elif 60<= int(i)< 70:
                seclow.append(i)
        elif 50<= int(i)< 60:
                third.append(i)
        elif 0<=int(i)<50:
                F.append(i)

print('1 |'+'X'*len(fir))
print('2+|'+'X'*len(secup))
print('2-|'+'X'*len(seclow))
print('3 |'+'X'*len(third))
print('F |'+'X'*len(F))

        