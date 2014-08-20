"""Assignment 6 Question 3
James Lloyd
21 April 2014"""

list=[]
myDic={}
print("Independent Electoral Commission")
print("--------------------------------")

#Get names in list
name=input("Enter the names of parties (terminated by DONE):\n")
while not name=="DONE":
    list.append(name)
    name=input()
    
#Iterate through names in list and add to dictionary
for i in list:
    if not i in myDic:
        myDic[i]=1
    else:
        myDic[i]+=1

#Print party and number of votes in sorted order    
print()
print("Vote counts:")
for key in sorted(myDic.keys()):
    print("{0:<11}".format(key),myDic[key],sep="- ") #column width of 10
    
    
        
    
    