"""Yashna Ravidas 
Calculating which students need to see student advisor
15 May 2014"""
import math
#filename=input("Enter the marks filename:\n")
#infile= open(filename, "r")
#lines = infile.read()
lines='Alan,35\nSiobhan,23\nMmberengeni,38'
line= lines.replace('\n',',')
arr=line.split(',')

def average(array):
    suma=0
    avg=0
    count=0    
    for i in range(1,len(array),2):
        a=int(array[i])
        suma=suma+a
        count+=1
        
    avg=(suma/count)        
    return avg     
        

def stddeviation(array,avg):
    import math
    count=0
    std=0
    stdv=0
    stddeviation=0
    for i in range(1,len(array),2):
        a=int(array[i])
        std=(avg-a)*(avg-a)
        stdv=stdv+std
        count+=1
        
    part1=(stdv/count)
    stddeviation=math.sqrt(part1)
    return round(stddeviation,2)


def advisor(array,avg,standard):
    for i in range(1,len(array),2):
        a=int(array[i])
        b=(avg-standard)
        if a-b<standard:
            return array[i-1]
    
    
print("The average is:",'%.2f'%average(arr))      
print("The std deviation is:",stddeviation(arr,average(arr)))
print("List of students who need to see an advisor:")
print(advisor(arr,average(arr),stddeviation(arr,average(arr))))





