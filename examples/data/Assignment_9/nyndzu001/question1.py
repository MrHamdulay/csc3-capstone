import math

textfile=input("Enter the marks filename:\n")

def main(textfile):
    sums=0
    names=[]
    namelist=[]
    counter=0
    count=0
    standard=0
    f=open(textfile,"r")
    lines=f.readlines()
    f.close()
    
    for line in lines:
        if line[-1]=='\n':
            line=line[:-1]
            names.append(line)
        line=line.split(',')
   
        sums+=eval(line[1])
        
      
        count+=1
    for i in names:
        i=i.split(',')   
        namelist.append(i)
    mean=sums/count
  
    
    for j in namelist:
        standard+=(eval(j[1])-mean)**2
        counter+=1
    
    sd=round(math.sqrt(standard/counter),2)
    
    print("The average is: {0:.2f}".format(mean))
    print("The std deviation is: {0:.2f}".format(sd))
    
    if sd>0:
        print("List of students who need to see an advisor:")
    for mark in namelist:
        if eval(mark[1])<(mean-sd):
            
            print(mark[0])

    
    
main(textfile)