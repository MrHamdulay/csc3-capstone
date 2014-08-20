list1=input("Enter a space-separated list of marks:\n")
list1=list1.split(" ")

for i in range(len(list1)):
    list1[i]=eval(list1[i])


count=[0,0,0,0,0]

for i in range(50):
    count[0]=count[0]+list1.count(i)

for i in range(50,60):
    count[1]=count[1]+list1.count(i)
    
for i in range(60,70):
    count[2]=count[2]+list1.count(i)

for i in range(70,75):
    count[3]=count[3]+list1.count(i)

for i in range(75,101):
    count[4]=count[4]+list1.count(i)
    
print("1 |","X"*count[4],sep="")
print("2+|","X"*count[3],sep="")
print("2-|","X"*count[2],sep="")
print("3 |","X"*count[1],sep="")
print("F |","X"*count[0],sep="")