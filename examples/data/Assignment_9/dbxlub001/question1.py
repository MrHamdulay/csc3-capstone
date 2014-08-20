"""marks affecting future
Lubalethu Dube
may 13 2014"""

def Mr_marks():
    import math
    filename=input("Enter the marks filename:\n")
    f=open(filename,"r")
    l1=f.read()
    #get marks
    l2=l1.replace("\n",",")
    l3=l2.split(",")
    f.close()
    marks=[]
    for i in range(len(l3)):
        if i%2!=0:
            marks.append(l3[i])
    #calculate average
    count=0
    sumy=0
    for i in marks:
        count+=1
        num=eval(i)
        sumy+=num
    av=(sumy/count)
    
    #calculate s. dev
    var=0
    count=0
    dp=[]
    for i in marks:
        num=eval(i)
        newy=(num-av)
        new1=(newy)*(newy)
        var+=new1
        count+=1

    st=math.sqrt((var)/count)
    #DP list
    i=1
    for i in range(len(l3)):
        if i%2 !=0:
            num=(eval(l3[i]))

            if num<av:
                i=i-1

                dp.append(l3[i])
    
    print("The average is:","%.2f"%av)
    print("The std deviation is:","%.2f"%st)
    if dp!=[]:
        
        print("List of students who need to see an advisor:")
        for i in dp:
            print(i)

Mr_marks()