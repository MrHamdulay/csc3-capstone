"""program to take in a list of marks and draw a histogram representation
by Tinashe Choga
23/04/2014"""
def histogram():
    marks=input("Enter a space-separated list of marks:\n")
    marks_list=marks.split(" ")
    #creating variables to store number of candidates in different mark ranges
    n=[]
    k=[]
    m=[]
    p=[]
    v=[]
    # sorting the marks
    for i in marks_list:
        if eval(i) >=75:
            n.append(i)
        elif 70<=eval(i) <75:
            k.append(i)
        elif 60<=eval(i)<70:
            m.append(i)
        elif 50<=eval(i)<60:
            p.append(i)
        elif eval(i)<50:
            v.append(i)
            #printing out the result
    print("1 |","X"*len(n), sep="")
    print("2+|","X"*len(k), sep="")
    print("2-|","X"*len(m), sep="")
    print("3 |","X"*len(p), sep="")
    print("F |","X"*len(v), sep="")
histogram()
    
        