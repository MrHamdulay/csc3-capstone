x=['']
maxlen = 0
print("Enter strings (end with DONE):")
cnt=0
while x[-1]!="DONE":
     x.append(input())
     if maxlen<len(x[cnt]):
          maxlen=len(x[cnt])
     cnt=cnt+1
print("\nRight-aligned list:")
for i in range(1,len(x)-1,1):
     print(x[i].rjust(maxlen))

