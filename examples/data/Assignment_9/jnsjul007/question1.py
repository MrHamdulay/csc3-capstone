#Julian van Rensburg
#Assignment 9 Q1
#files bruuu
#12/05/2014

#open the file bruuu
import math
file=input("Enter the marks filename:\n")
f=open(file,"r")
lines=f.readlines

#define the marks and names from the information in file
Mark=0
count=0  
dictionary={}
av=0
#send names and marks to a dictionary
for lines in f:
            for i in range(len(lines)):
                        if lines[i]==",":
                                    name= lines[:-(len(lines)-i)]
                                    mark= lines[i+1:]
                                    count+=1
                                    dictionary.update({name:int(mark)})
                                    tote_mark= Mark + int(mark)
                                    Mark=tote_mark
                                    av=tote_mark/count
                                    
print("The average is:","{:0.2f}".format(av))
var2= 0                                   
count1=0
#calculate STD Deviation from the dictionary
for items in dictionary:
            value= dictionary[items]        
            var1=(value-av)**2      
            var2+=var1
            count1+=1
var=math.sqrt(var2/count1)
print("The std deviation is:","{:0.2f}".format(round(var,2)))


t=0
f.close()
#open file again to run loop
f=open(file,"r")
lines=f.readlines
for items in dictionary:
            if (av-var)> int(dictionary[items]):
                        t=1
                        
if t==1:
            print("List of students who need to see an advisor:\n",end='')
#run loop again to check if marks are below one STD deviation
for lines in f:
            for i in range(len(lines)):
                        if lines[i]==",":
                                    name= lines[:-(len(lines)-i)]
                                    mark= lines[i+1:]                                    
            if (av-var)>int(mark):
                        
                        print(name,sep='')
f.close()
          
                                                
                   