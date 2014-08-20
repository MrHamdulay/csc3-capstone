"""Pairs
Lubalethu Dube
8 May"""
count=0
pa=input("Enter a message:\n")
def pairs(pa):
    global count
    if len(pa)<= 1:
        print(count)
    elif pa[0]==pa[1]:
        count = count+ 1
        return pairs(pa[2:])
    else:
        return pairs(pa[2:])
    

print("Number of pairs: ",end="")
pairs(pa)               
    
        