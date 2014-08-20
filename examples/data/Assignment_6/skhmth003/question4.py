#Program for producing a histogram of marks that fall in different categories
#21/04/2014
#Gordon Skhosana

def mark_collection():
    """Function that collects marks and sorts them into different categories"""
    #Capturing the marks
    marks=input("Enter a space-separated list of marks:\n")
    marks=marks.split(" ")
    MARKS=[]
    #Converting marks from strings to integers
    for i in marks:
        j=int(i)
        MARKS.append(j)
    #Seperating marks into different categories
    counters=0
    global firsts
    global second_plus
    global second_minus
    global third
    global fail
    firsts=[]
    second_plus=[]
    second_minus=[]
    third=[]
    fail=[]
    for i in MARKS:
        if i>=75:
            firsts.append(i)
        elif i>=70:
            second_plus.append(i)
        elif i>=60:
            second_minus.append(i)
        elif i>=50:
            third.append(i)
        else: fail.append(i)
def count():
    """Function that counts the number of marks that fall into each category"""
    global firsts_count
    global sec_plus_count
    global sec_minus_count
    global thrd_count
    global fail_count
    #Firsts
    firsts_count=0
    for i in firsts:
        firsts_count+=1
    #Second_plus
    sec_plus_count=0
    for i in second_plus:
        sec_plus_count+=1
    #Second_minus
    sec_minus_count=0
    for i in second_minus:
        sec_minus_count+=1    
    #Third
    thrd_count=0
    for i in third:
        thrd_count+=1    
    #Fail
    fail_count=0
    for i in fail:
        fail_count+=1
def histogram():
    """Function that produces a histogram of marks according to the categories in which they fall"""
    mark_collection()
    count()
    print("1 |","X"*firsts_count,sep="")
    print("2+|","X"*sec_plus_count,sep="")
    print("2-|","X"*sec_minus_count,sep="")
    print("3 |","X"*thrd_count,sep="")
    print("F |","X"*fail_count,sep="")
histogram()
