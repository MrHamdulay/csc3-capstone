'''Mokoena mafologele
histogram program
22/04/2014'''

marks=input("Enter a space-separated list of marks:\n").split(" ") #Get marks input from user
numbers_list={'fail':[],'third':[],"lower":[],"upper":[],"first":[]}
#group by interval
for i in marks:
    j=int(i)
    if j<50:
        numbers_list['fail'].append(j)
    elif j<60:
        numbers_list['third'].append(j)
    elif j<70:
        numbers_list['lower'].append(j)
    elif j<75:
        numbers_list['upper'].append(j)
    else:
        numbers_list['first'].append(j)
#display histogram
print("1 |","X"*len(numbers_list['first']),sep="")
print("2+|","X"*len(numbers_list['upper']),sep="")
print("2-|","X"*len(numbers_list['lower']),sep="")
print("3 |","X"*len(numbers_list['third']),sep="")
print("F |","X"*len(numbers_list['fail']),sep="")
        
