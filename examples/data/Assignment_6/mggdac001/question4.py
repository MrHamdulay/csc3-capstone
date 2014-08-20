def hist():
    mark_l=[]
    mark_dictionary={}
    mark_i=input('Enter a space-separated list of marks:\n')
    for mark in (mark_i.split()):
        mark_l.append(mark)
    #print("length",len(mark_l))
    n=0
    f=0
    first=0
    third=0
    lower=0
    upper=0
    while n<len(mark_l):
        
        if (eval(mark_l[n]))<50:
            f+=1
        elif 50<=(eval(mark_l[n]))<60:
            third+=1
        elif 60<=(eval(mark_l[n]))<70:
            lower+=1
        elif 70<=(eval(mark_l[n]))<75:
            upper+=1
        elif (eval(mark_l[n]))>=75:
            first+=1
    
        n+=1
    mark_dictionary[f]=f
    mark_dictionary[third]=third
    mark_dictionary[lower]=lower
    mark_dictionary[upper]=upper
    mark_dictionary[first]=first    
    
    print('1 |',(mark_dictionary[first])*'X',sep='')
    print("2+|",mark_dictionary[upper]*'X',sep='')
    print("2-|",mark_dictionary[lower]*"X",sep='')
    print('3 |',mark_dictionary[third]*"X",sep='')
    print('F |',(mark_dictionary[f])*'X',sep='')
           
        
        
    
hist()    
    