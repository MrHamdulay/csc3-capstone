def marks():
    marks=[]
    x= input('Enter a space-separated list of marks:\n')
    a = x.split()
    
    for i in a:
            x=int(i)
            marks.append(x) 
            
    return marks
    
def graph(l):
    frst=0
    up2nd=0
    low2nd=0
    thrd=0
    fail=0
    
    for i in l:
        if i >=75 and i<=100:
            frst=frst+1
        elif i >=70 and i<=100:
            up2nd=up2nd+1            
        elif i >=60 and i<=100:
            low2nd=low2nd+1   
        elif i >=50 and i<=100:
            thrd=thrd+1
        elif i<50:
            fail=fail+1
        else:
            continue
    print('1 |',('X'*frst),sep='')
    print('2+|',('X'*up2nd),sep='')
    print('2-|',('X'*low2nd),sep='')
    print('3 |',('X'*thrd),sep='')
    print('F |',('X'*fail),sep='')
    
list=marks()
graph(list)