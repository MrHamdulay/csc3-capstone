#program to create histogram of marks in each grade class
#Kayla Hendricks
#23 April 2014

def mark_list():
    #create empty lists for each grade
    first=[]
    upsec=[]
    lowsec=[]
    third=[]
    fail=[]
    input_marks = input("Enter a space-separated list of marks:\n")
    
    #split marks up and evaluate individually
    for j in input_marks.split(" "):
        mark=eval(j)
        if mark>=75:
            first.append("X")
        elif mark>=70:
            upsec.append("X")
        elif mark>=60:
            lowsec.append("X")
        elif mark>=50:
            third.append("X")
        else:
            fail.append("X")
    
    #if lists have items in them, print the contents
    if len(first)>0:
        print("1 |","X"*first.count("X"),sep="")
    else: 
        print("1 |")
    if len(upsec)>0:
        print("2+|","X"*upsec.count("X"),sep="")
    else:
        print("2+|")
    if len(lowsec)>0:
        print("2-|","X"*lowsec.count("X"),sep="")
    else:
        print("2-|")
    if len(third)>0:
        print("3 |","X"*third.count("X"),sep="")
    else:
        print("3 |")
    if len(fail)>0:
        print("F |","X"*fail.count("X"),sep="")
    else:
        print("F |")
        
mark_list()
        
    
    
    
    