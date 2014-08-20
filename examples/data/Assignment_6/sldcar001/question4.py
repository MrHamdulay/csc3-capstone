def marks():
    ip=input("Enter a space-separated list of marks:\n")
    line=ip.split()
    one=[]
    tup=[]
    tlow=[]
    three=[]
    F=[]
    op=''

    for i in line:
        a=i
        if eval(a)<50:
            F.append(a)
        elif eval(a)<60:
            three.append(a)
        elif eval(a)<70:
            tlow.append(a)  
        elif eval(a)<75:
            tup.append(a) 
        else:
            one.append(a)
    print("1 |","X"*len(one),sep='')
    print("2+|","X"*len(tup),sep='')
    print("2-|","X"*len(tlow),sep='')
    print("3 |","X"*len(three),sep='')
    print("F |","X"*len(F),sep='')
marks()
    