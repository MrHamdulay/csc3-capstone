def analyse(line):
    a=line.split(",")
    mark=a[1].replace('\n','')
    return(mark,a[0])
    
    
import math
def decider():
    filename=input("Enter the marks filename:\n")
    f=open(filename,"r")
    #print(f.read())
    marklist=[]
    cnt=0
    std_cnt=0
    stdtlist=[]
    ind_cnt=0
    out="{0:.2f}"
    df=[]
    for line in f.readlines():
        mark,stdt=analyse(line[0:len(line)])
        marklist.append(eval(mark))
        stdtlist.append(stdt)
    for i in marklist:
        cnt+=i
    average=cnt/len(marklist)
    print("The average is:",out.format(average))
    for i in marklist:
        std_cnt+=(i-average)**2
    stdd=math.sqrt(std_cnt/len(marklist))
    print("The std deviation is:",out.format(stdd))
    for i in marklist:
        if i<average-stdd:
            df.append(stdtlist[ind_cnt])
        ind_cnt+=1
    if len(df)>0:
        print("List of students who need to see an advisor:")
        for i in df:
            print(i)
    f.close()

    
decider()