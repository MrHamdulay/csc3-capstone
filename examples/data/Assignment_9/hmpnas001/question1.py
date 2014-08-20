"""progam to get marks
nasonkwe hampwaye
2014-05-14"""
import math

def marks():
    #opening and viewing data
    filename=input("Enter the marks filename:\n")
    f=open(filename,"r")
    lines=f.readlines()
    f.close
    #getting marks average
    add=0
    count=0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]==",":
                add+=int(lines[i][j+1:])
                count+=1
    ave=add/count 
    print("The average is:",'%.2f'%(ave))
    #standard deviation
    sum_d=0
    for i in range(len(lines)):
        for j in range (len(lines[i])):
            if lines[i][j]==",":
                sum_d+=(int(lines[i][j+1:])-ave)**2
    std_dev=math.sqrt(sum_d/count)
    print("The std deviation is:",'%.2f'%(std_dev))
    #who sees advisor???
    if std_dev>0:
        print("List of students who need to see an advisor:")
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j]==",":
                    if int(lines[i][j+1:])<ave-std_dev:
                        print(lines[i][:j])
    
marks()    
                
            
    