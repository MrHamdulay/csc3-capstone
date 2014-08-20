"""Shahrain Coovadia"""

import math 

def marks(files):
    f=open(files,"r")
    lines=f.readlines()
    f.close()
    y=eval(average(file))
    stnd=eval(standard_deviation())
    inp=[]
    for i in lines:
        if i[-1]=='\n':          
            i=i[:-1]
        x=i.split(",")
        mrk=eval(x[1])
        if mrk < y-stnd:
            inp.append(x[0])
        return inp

def standard_deviation(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    x=0
    for i in lines:
        x+=1
    y=eval(average(file))
    s=0
    for l in lines:
        if l[-1]=="\n":
            l=l[:-1]
        l=l.split(",")
        s+=(eval(l[1])-y)**2
    stnd=str(round(math.sqrt(s/x),2))
    return stnd


   
    
    
def main():
    file=input("Enter the marks filename:\n")
    print("The average is:", "{0:0,5}".format(average(file)))
    print("The std deviation is:", "{{0:0<4}".format(standard_deviation(file)))
    m=marks(file)
    if m:
        print("List of students who need to see an advisor:")
        for i in m:
            print(i)
main()

    
            
