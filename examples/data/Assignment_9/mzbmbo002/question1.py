#Mbongeni Mazibuko
#MZBMBO002
#Assignment 9 Q1

import math

file= input("Enter the marks filename:\n")
f= open(file,'r')
marks=[]
N=0
total=0

for line in f:
    comma= line.find(',')
    #locate marks by finding them after the comma
    marks.append(line[comma+1:-1])
    #Add mark to list
    N+=1
f.close()
mean= eval('+'.join(marks))/N
#divide total by number of marks

for mark in marks:
    #go through each mark to find 'mark - mean' squared and add that to the total
    total+= (int(mark)-mean)**2
    
s_dev= math.sqrt(total/N)
#divide 'total' by number of marks to find standard deviation
print("""The average is: """ + '{0:.2f}'.format(mean)+
"""\nThe std deviation is: """ +'{0:.2f}'.format(s_dev))
f= open(file,'r')
names=''
advisor='no'
#students who need to see advisor is false since the marks haven't been analised yet

for line in f:
    comma= line.find(',')
    if int(line[comma+1:comma+3])<(mean-s_dev):
        names+=line[:comma]+'\n'
        #name added to list of students who need to see advisor
        advisor='yes'
        #advisor is set to yes when students mark is less than one standard deviation below the mean
        
if advisor=='yes':        
    print("""List of students who need to see an advisor:\n"""+ names)   
f.close()