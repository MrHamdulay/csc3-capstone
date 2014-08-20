import math
def getFileContent(filename):
    f=open(filename,"r")
    content=f.readlines()
    f.close()
    return content
def findMean(arrMarks):
    average=0
    for i in range(len(arrMarks)):
        mark=float(arrMarks[i].split(",")[1])
        average+=mark
    average/=len(arrMarks)
    return average
def findSdeviation(arrMarks,mean):
    dev=0
    for i in range(len(arrMarks)):
        mark=float(arrMarks[i].split(",")[1])
        dev=dev+math.pow((mark-mean),2)
    dev=math.sqrt(dev/len(arrMarks))
    return dev
def check(arrMarks,mean,dev):
    advisorList=[]
    rang=mean-dev
    for i in range(len(arrMarks)):
        mark=float(arrMarks[i].split(",")[1])
        if mark<rang:
            advisorList.append(arrMarks[i].split(",")[0])
    return advisorList
def main():
    filename=input("Enter the marks filename:\n")
    arrContent=getFileContent(filename)
    mean=findMean(arrContent)
    deviation=findSdeviation(arrContent,mean)
    advisorList=check(arrContent,mean,deviation)
    print("The average is: ",("%0.2f")%(mean),"\nThe std deviation is: ",("%0.2f")%(deviation),"\nList of students who need to see an advisor:",sep="")
    for i in advisorList:
        print(i)
if __name__ == "__main__":
    main()
    
    