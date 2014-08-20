# histogram of marks
# Soahil Tulsi TLSSOH001
# 23 April 2014

marks= []

#inpuit string values
mark=input('Enter a space-separated list of marks:\n')
strmarks = mark.split(' ')
F = 0
third = 0
first = 0
secondps =0
secondmn = 0
#create for statement that seperate
for i in range(len(strmarks)):

    
    if eval(strmarks[i]) >= 75:
        first += 1
    elif 70 <= eval(strmarks[i]) <75:
        secondps += 1
    elif 60 <= eval(strmarks[i]) < 70:
        secondmn += 1
    elif 50 <= eval(strmarks[i]) < 60:
        third += 1
    else:
        F += 1

#print the variables that apply for that supposed avriable other functions yay

print('1 |','X'*first,sep='')
print('2+|','X'*secondps,sep='')
print('2-|','X'*secondmn,sep='')
print('3 |','X'*third,sep='')
print('F |','X'*F,sep='')