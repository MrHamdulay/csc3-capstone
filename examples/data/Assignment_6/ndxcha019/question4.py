'''Luke Naudé
2014-04-24
program to creat a histogram representing class marks'''

#get string input of marks
mark_string=input('Enter a space-separated list of marks:\n')


#turn string into list
mark_list=mark_string.split(' ')

Fail=[]
Third=[]
LowerSecond=[]
UpperSecond=[]
First=[]

#append each mark into it's category
for i in mark_list:
    if eval(i) < 50:
        Fail.append(i)
    elif 50 <= eval(i) < 60:
        Third.append(i)
    elif 60 <= eval(i) < 70:
        LowerSecond.append(i)
    elif 70 <= eval(i) < 75:
        UpperSecond.append(i)
    elif 75 <= eval(i):
        First.append(i)

#print each category with X's denoting count
print('1 |','X'*len(First),sep='')
print('2+|','X'*len(UpperSecond),sep='')
print('2-|','X'*len(LowerSecond),sep='')
print('3 |','X'*len(Third),sep='')
print('F |','X'*len(Fail),sep='')