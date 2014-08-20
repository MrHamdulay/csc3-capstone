"""a histogram representation of marks
Kamogelo Mphela
20 April 2014"""

# collect the list of marks from the user
marks = []
x = input("Enter a space-separated list of marks:\n")
m = x.split()
for i in m:
    x =eval(i)
    marks.append(x)

# sort the marks in their respective groups

counters=[0,0,0,0,0]
for i in marks:
    for j in counters:
        if i >=75:
            counters[0]+=1
        elif i >= 70:   
            counters[1]+=1
        elif i >= 60:
            counters[2]+=1
        elif i >= 50:
            counters[3]+=1
        else:   
            counters[4]+=1
        break

# print them out in a histogram 
print("1 |","X"*counters[0],sep="")
print("2+|","X"*counters[1],sep="")
print("2-|","X"*counters[2],sep="")
print("3 |","X"*counters[3],sep="")
print("F |","X"*counters[4],sep="")