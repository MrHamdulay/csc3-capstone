#Categorize 
def categorize(x):
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in x:
        i=eval(i)
        if i>=75:
            a+=1
        elif 70<=i<75:
            b+=1
        elif 60<=i<70:
            c+=1
        elif i>=50:
            d+=1
        else:
            e+=1
    grades=[a,b,c,d,e]
    return grades




#Get list
marks=input("Enter a space-separated list of marks:\n").split(" ")
results=(categorize(marks))

#Histrogram
#print("12 23 34 45 56 67 78 89 90")
print("1 |", "X"*results[0],sep='')
print("2+|", "X"*results[1],sep='')
print("2-|", "X"*results[2],sep='')
print("3 |", "X"*results[3],sep='')
print("F |", "X"*results[4],sep='')
