"""List of students to see student advisor-Deviation below mean
Dudley Mutero
15/5/14"""

import math

list1=[]                                #thi is where we collect student marks and calculate deviation and mean
a=input("Enter the marks filename:\n")  #a is the variable the filename will be stored
filing= open (a,"r")
for i in filing:
    b=i.find(",")                #b is a position of the comma
    c= i[b+1::]                  #c is we slice the word to look for the mark of the student 
    list1.append(eval(c))        #appending student marks list1
filing.close()


#working out the mean
mean=0                              #mean is a variable where the summation of the mean is
for i in list1:
    mean+=i
    
e=len(list1)                        #e is the length of list1
average= mean/e 

#working out the deviation
list2=[]
for j in list1:
    k=(j-average)**2                # k is a temporary variable
    list2.append(k)
    
list2summation=0
for l in list2:
    list2summation+=l
    
m=len(list2)                        #m is the value of length of list2
deviation=math.sqrt(list2summation/m)
meandeviation=average-deviation



list3=[]
infile=open(a,'r')
#names of students with names less than deviation
for p in infile:
    n=p.find(",")
    A=eval(p[n+1:n+3])
    if A < meandeviation:
        list3.append(p[0:n])
infile.close()



#printing part
average = "%.2f"%round(average,2)
deviation = "%.2f"%round(deviation,2) #formatting to 2 decimal places even with zeros
print('The average is:',average)
print("The std deviation is:",deviation)
if len(list3)>0:
    print("List of students who need to see an advisor:")
    for q in list3:
        print (q)
    

    
    
    
    
    
