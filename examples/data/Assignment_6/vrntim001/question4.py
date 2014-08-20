'''Histogram
Tim Mostert
23/4/14'''
numbers = input("Enter a space-separated list of marks:\n")
thelist = numbers.split()
first,uppersecond,lowersecond,third,fail = 0,0,0,0,0


for i in thelist:
    p = eval(i)
    if p < 50:
        fail += 1
    elif 50 <= p < 60:
        third += 1
    elif 60 <= p < 70:
        lowersecond += 1
    elif 70 <= p < 75:
        uppersecond += 1
    else:
        first += 1


print("1 |", "X"*first,sep='')       
print("2+|", "X"*uppersecond,sep='')
print("2-|", "X"*lowersecond,sep='')
print("3 |", "X"*third,sep='')
print("F |", "X"*fail,sep='')


