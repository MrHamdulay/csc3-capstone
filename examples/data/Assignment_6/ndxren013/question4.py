#Reneshan Naidoo
#Make Histograms

marks = list(map(int, input('Enter a space-separated list of marks:\n').split()))
#read in marks

mystrings = ['1 |', '2+|', '2-|', '3 |', 'F |']
#begin outputs

for i in marks:
    if i < 50:
        mystrings[4] += 'X'
    elif 50 <= i < 60:
        mystrings[3] += 'X'
    elif 60 <= i < 70:
        mystrings[2] += 'X'
    elif 70 <= i < 75:
        mystrings[1] += 'X'
    else:
        mystrings[0] += 'X'
#add to appropriate places

for i in mystrings:
    print(i)
#output answers
