'''Luke Joseph
2014-05-13
Question 1 of assignment 9'''

import math
def main():
    y=[]
    f=input("Enter the marks filename:\n")
    f=open(f,"r")
    y=f.readlines()
    f.close()
    #print(y)
    nos=[]
    tot=0
    dev=0
    newlist=[]
    p=0
    
    for i in range(len(y)): # Loop spliiting numbers and names into a list
        newlist+=y[i].split(",")

      
    
    for i in range(1,len(newlist),2):# Loop appending only numbers to a list
        x=newlist[i]
        #x=eval(x)
        nos.append(eval(x[:-1]))
        
    for j in range(len(nos)):# Loop performing average calculation
        tot+=nos[j]
    ave=tot/len(nos)
    print("The average is: {0:5.2f}".format(ave))
    
    for j in range(len(nos)): # Loop performing standard deviation calculation
        dev+=(nos[j]-ave)*(nos[j]-ave)
    stddev=math.sqrt(dev/len(nos))
    print("The std deviation is: {0:4.2f}".format(stddev))
    
    for i in range(len(nos)): # Loop to see if anyone should see counsellor
        if nos[i]<(ave-stddev):
            p=1
        else:
            pass
            
    if p==1:
        print("List of students who need to see an advisor:")
    
    for i in range(len(nos)): # Loop printing names of those who should see counsellor
        if nos[i]<(ave-stddev):
            print(newlist[i+i])
        else:
            pass
main()