def countpairs(string,x):
    if len(string)==0 or len(string)==1:             # pyhon MRU pg45
        return print("Number of pairs:",x)

    elif string[0]==string[1]:
        x+=1
        return countpairs(string[2:],x)
    else:
        return countpairs(string[2:],x)
string=input("Enter a message:\n")
countpairs(string,0)

#moves to the next two charaters


