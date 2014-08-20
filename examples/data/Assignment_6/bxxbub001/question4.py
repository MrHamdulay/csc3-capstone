#marks
#B.Booi
#24 April

def marks():
    fail = 0
    thirds = 0
    lower2 = 0
    upper2 = 0
    first = 0
    numbers = input("Enter a space-separated list of marks:\n")
    numb_list=numbers.split(" ")
    #print(numb_list)
    listlen = len(numb_list)
    #print("length",listlen)
    for x in range(listlen):
        num = eval(numb_list[x])
        if num < 50:
            fail +=1
        elif num <60:
            thirds +=1
        elif num <70:
            lower2 +=1
        elif num <75:
            upper2 +=1
        elif num<= 100:
            first +=1
    
    print("1 |","X"*first,sep="")
    print("2+|","X"*upper2,sep="")
    print("2-|","X"*lower2,sep="")
    print("3 |","X"*thirds,sep="")
    print("F |","X"*fail,sep="")
            
            
        


marks()
        