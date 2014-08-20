#Assignment 6
#Question 4
#Due Date: 25/04/14
#Rabia Parker

#Program to output a list of marks in the form of a histogram


f=0
first =0
upSec=0
lowSec=0
thrd=0
lst=[]
List=input("Enter a space-separated list of marks:\n")
lst=List.split()#Separating the values in the string into a list
    
for i in range(len(lst)): #running each item in list
            if eval(lst[i]) >= 75:
                        first = first+ 1
            elif 70 <= eval(lst[i]) < 75:
                        upSec = upSec + 1
            elif 60 <= eval(lst[i]) < 70:
                        lowSec = lowSec + 1
            elif 50 <= eval(lst[i]) < 60:
                        thrd = thrd + 1
            elif eval(lst[i]) < 50:
                        f=f+1 
#printing histogram

print("1 |", 'X'*first,sep="")
print("2+|", 'X'*upSec,sep="")
print("2-|", 'X'*lowSec,sep="")
print("3 |", 'X'*thrd,sep="")
print("F |", 'X'*f,sep="")        
    
    
