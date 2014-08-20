"""Shriya Roy
14 MAy 2014
program to compute standard deviation"""

import math

def main():

    count = 0
    
    name =input("Enter the marks filename: \n")
    f=open(name,"r")
    line=f.readlines()
    
    x = []
    mark = []    
    
    for i in range (len(line)):
        
        
            comma = line[count].index(",")
            count+=1
            
            
            x.append(line[i][0:comma])
            
            mark.append(line[i][(comma+1):(len(line[i]))])
    sum_=0
    for i in range (len(mark)):
        happy=eval(mark[i])
        sum_+=happy
        
    average=sum_/len(mark)
    
    add=0
    
    for i in range(len(mark)):
        dev=(eval(mark[i])-average)**2
        
        add+=dev
        
    result=math.sqrt(add/len(mark))
    
    print("The average is: {0:.2f}".format(average))
    print("The std deviation is: {0:.2f}".format(result))
    
    z=[]
    for i in range(len(mark)):
        if eval(mark[i])<(average-result):
            z.append(x[i])
            
            
    if len(z)>0:
        print("List of students who need to see an advisor:")
        for i in range(len(z)):
            print(z[i])
            
    else:
        print()
            
            

        
        
                
    
    
    
        
        
        
    
        
        
            
    f.close()

main()
    

    
