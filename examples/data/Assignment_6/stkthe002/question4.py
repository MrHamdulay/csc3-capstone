#Thea Sitek, STKTHE002
#18.05.2014
#Histogram over grades

marks = input('Enter a space-separated list of marks: \n')
marks = marks.split(' ')

grades = ['1','2+','2-','3','F']
counter = [0,0,0,0,0]

#strings into integers
marksint = []
#...but with numerical values
for i in range(len(marks)):
    marksint.append(int(marks[i])) 

#delegate marks into grades        
for i in marksint:
    if i > 100 or i < 0:
        continue
    elif i >= 75:
        counter[0] += 1
    elif i >= 70:
        counter[1] += 1
    elif i >= 60:
        counter[2] += 1          
    elif i >= 50:
        counter[3] += 1            
    else:
        counter[4] += 1
                    
space = 2  
#format and print
for i in range(5):
    space -= len(grades[i])
    print(grades[i], ' '*space, '|', 'X'*counter[i], sep="")
    space = 2
    
