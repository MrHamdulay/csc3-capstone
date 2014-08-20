string = input("Enter a space-separated list of marks:\n")
string = string.split()
list_1 = (string)

fail = []
third = []
down2 = []
up2 = []
first = []
t = 0
for i in list_1:
    if int(list_1[t]) < 50:
        fail.append(int(list_1[t]))
    elif 50 <= int(list_1[t]) < 60:
        third.append(int(list_1[t]))
    elif 60 <= int(list_1[t]) < 70:
        down2.append(int(list_1[t]))
    elif 70 <= int(list_1[t]) < 75:
        up2.append(int(list_1[t]))
    elif int(list_1[t]) >= 75:
        first.append(int(list_1[t]))
    t+=1
    
fail = len(fail)
third = len(third)
down2 = len(down2)
up2 = len(up2)
first = len(first)
print("1 |","X"*first,sep='')
print("2+|","X"*up2,sep='')  
print("2-|","X"*down2,sep='')  
print("3 |","X"*third,sep='')  
print("F |","X"*fail,sep='')  
        