print("Enter strings (end with DONE):")
list=input("")
ary=[list]
while list != "DONE" :
    list=input("")
    ary.append(list)
while list != "DONE" :
    break
length=len(ary)
ary=ary[0:length-1]
dp=ary*1
dp.reverse()

for i in dp:
    while dp.count(i)>1:
        dp.remove(i)
dp.reverse()
print("\n""Unique ist:")
for i in dp:
    print(i)