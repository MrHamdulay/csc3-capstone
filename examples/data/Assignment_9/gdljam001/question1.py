"""James Godlonton
marks checker
10 May 2014"""

#Sample I/O

#Enter the marks filename:
#test1.txt
#The average is: 32.00
#The std deviation is: 6.48
#List of students who need to see an advisor:
#Siobhan

import math
def listStudents(allStudents):
    """Gets a list of all students and their marks together, returns a list of [<average>,<std>,st1,st2...] where st1 etc are students who get below one std away from average"""
    retList=[]
    markSplit=[]
    for st in range (len(allStudents)):
        #Goes through students in list then splits them into a dictionary of mark and name then adds it to the split list
        dict={"name": allStudents[st][0:allStudents[st].find(",")], "mark": int(allStudents[st][allStudents[st].find(",")+1:])}
        markSplit.append(dict)
    average=0
    
    for i in markSplit:
        #Goes through all marks in list of dictionaries adds them up and divides by total (gets average)
        average=average+i["mark"]
    average=average/len(markSplit)
    stdDev=0
    for i in markSplit:
        #goes through all marks in list of dictionaries adds up the difference between each mark and average squared for all marks
        stdDev=stdDev+(i["mark"]/1-average)**2
    stdDev=math.sqrt(stdDev/len(markSplit))#Takes squareroute of total/number of marks as to calculate standard deviation
    retList.append(str(round(average,2)))#Adds average to return list
    retList.append(str(round(stdDev,2)))#Add std to return list
    for i in markSplit:
        #Goes through all marks and if mark is below one std below average then adds the corresponding name to return list
        if i["mark"]<(average-stdDev):
            retList.append(i["name"])
    return retList
def main():
    """Main function for input and output management"""
    fileName=input("Enter the marks filename:\n")
    f=open(fileName,"r")#Opening speified file
    allStudentsA=[]
    for i in f:#Append every line to the array of students
        allStudentsA.append(i)
    f.close() #Close file asap
    prints=listStudents(allStudentsA)#Get a list of what to print from listStudents function
    while len(prints[0][prints[0].find(".")+1:])<2: #2 while loops to insure std and average are printed with 2 digits after full stop
        prints[0]=prints[0]+"0"
        
    while len(prints[1][prints[1].find(".")+1:])<2:
        prints[1]=prints[1]+"0"
    
    
    print("The average is: "+prints[0])#Printing average then std
    print("The std deviation is: "+prints[1])
    if len(prints)>2:#If there are students in array (any elements in 2 or after) then output them
        print("List of students who need to see an advisor:")
        for i in range (2,len(prints)):
            print(prints[i])
        
if __name__=="__main__":
    main()
        
    
        