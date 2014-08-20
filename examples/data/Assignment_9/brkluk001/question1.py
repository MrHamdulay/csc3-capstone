file_name = input('Enter the marks filename: \n')
f = open(file_name, 'r')
list1 = f.readlines()
for i in range(len(list1)):
    if list1[i][-1] == '\n':
        list1[i] = list1[i][:-1]
        
total_marks =0        
for i in list1:
    pos = i.find(',')
    mark = eval( i[pos+1:])
    total_marks+=mark
    
mean = total_marks/len(list1)

variance = 0
for i in list1:
    pos = i.find(',')
    mark = eval( i[pos+1:])
    variance+= ((mean - mark)**2)
import math    
std_deviation = math.sqrt(variance/len(list1))
    
print('The average is:', '{0:^5.2f}'.format(mean))
print('The std deviation is:', '{0:^5.2f}'.format(std_deviation)) 

j=0
for i in list1:
    
    pos = i.find(',')
    mark = eval( i[pos+1:])
    
    if mark < (mean - std_deviation):
        if j==0:
            print('List of students who need to see an advisor:')
            print(i[:pos])
            j+=1
        else: 
            print(i[:pos])
        
        
            
        
        
      


    
    
    

