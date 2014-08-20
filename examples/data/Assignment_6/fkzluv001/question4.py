inpt=input("Enter a space-separated list of marks:\n").split(" ") #allow user to enter marks
numList={'fail':[],'third':[],"lower":[],"upper":[],"first":[]}
#group marks by interval
for i in inpt:
    j=int(i)
    if j<50:
        numList['fail'].append(j)
    elif j<60:
        numList['third'].append(j)
    elif j<70:
        numList['lower'].append(j)
    elif j<75:
        numList['upper'].append(j)
    else:
        numList['first'].append(j)
#print marks by class/interval
print("1 |","X"*len(numList['first']),sep="")
print("2+|","X"*len(numList['upper']),sep="")
print("2-|","X"*len(numList['lower']),sep="")
print("3 |","X"*len(numList['third']),sep="")
print("F |","X"*len(numList['fail']),sep="")
        