'''Analyse student marks read in from a file and determine which students need to see a student advisor
Nokosoftonic
May 2014'''

#open file for reading
filename = input('Enter the marks filename:\n')
f = open(filename)
records=[]
names=[]
marks=[]

while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        records+=line.split(',')
        
for n in records:
    if '\n' in n:
        n.replace(n,n[:-2])
        marks.append(eval(n))
    elif n.isdigit():
        marks.append(eval(n))
    else: names.append(n)
        
f.close()


#do calculations
import math

def min_std(lst): 
    std=0
    total = 0
    n =len(lst)
    
    #add-up scores
    for mark in lst:
        total += mark
        
    # sum up num - mean squared
    for num in lst:
        std+=(num-total/n)**2 
    
    print('The average is:','{0:0.2f}'.format(total/n)) 
    print('The std deviation is:','{0:0.2f}'.format(math.sqrt(std/n)))
    
    #check scores below std
    if math.sqrt(std/n) !=0:
        print('List of students who need to see an advisor:')
    pos=0
    for mark in marks:
        if mark<((total/n)-(math.sqrt(std/n))):
            print(names[pos])
            pos+=1
        else:
            pos+=1
            
min_std(marks)