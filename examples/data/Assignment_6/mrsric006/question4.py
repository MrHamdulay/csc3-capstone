def q4():
    j = []
    strlist = input("Enter a space-separated list of marks:\n")
    l = (strlist.split(" "))
   
    for i in l:
        i = eval(i)
        j.append(i)
    
    first = 0
    upsecond = 0 
    losecond = 0
    third = 0
    fail = 0
    
    for k in j:
        if k >= 75:
            first += 1
        elif 70 <= k < 75:
            upsecond += 1
        elif 60 <= k < 70:
            losecond += 1
        elif 50 <= k < 60:
            third += 1
        else:
            fail += 1
        
    print("1 |","X"*first,"\n","2+|","X"*upsecond,"\n","2-|",'X'*losecond,"\n","3 |",'X'*third,"\n","F |","X"*fail,sep='')
        
q4()