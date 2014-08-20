#A program to output a histogram of marks according to UCT mark catagories 
#Created by:Jenna Lake
#Date: 25/4/2014

def get_string():
    list_space=input("Enter a space-separated list of marks:\n")
    listA=[]
    for i in list_space.split():
        listA.append(i)

#def assign():
    newlist=[]
    for i in listA:                 #checks what catagory each inputed mark falls into
        t=int(i)
        if t>=75:
            newlist.append("1 ")
        if 75>t>=70:
            newlist.append("2+")
        if 70>t>=60:
            newlist.append("2-")
        if 60>t>=50:
            newlist.append("3 ")
        if 50>t:
            newlist.append("F ")

#def count():                       #counts the number of marks falling within each catagory
    a=newlist.count("1 ")
    b=newlist.count("2+")
    c=newlist.count("2-")
    d=newlist.count("3 ")
    f=newlist.count("F ")
    
#def format():                      #prints formatted version
    print("1 ", "|", "X"*a,sep="")
    print("2+", "|", "X"*b,sep="")
    print("2-", "|", "X"*c,sep="")
    print("3 ", "|", "X"*d,sep="")
    print("F ", "|", "X"*f,sep="")
    
get_string()