x = input("Enter a space-separated list of marks:\n")
x = x.split(" ")
for i in range(0,len(x),1):
    x[i]=int(x[i])
cnt = [0,0,0,0,0]
for i in range(0,len(x),1):
    if x[i]<50:
        cnt[0]+=1
    elif x[i]<60:
        cnt[1]+=1
    elif x[i]<70:
        cnt[2]+=1
    elif x[i]<75:
        cnt[3]+=1
    else:
        cnt[4]+=1
print("1 |"+"X"*cnt[4])
print("2+|"+"X"*cnt[3])
print("2-|"+'X'*cnt[2])
print("3 |"+'X'*cnt[1])
print("F |"+'X'*cnt[0])