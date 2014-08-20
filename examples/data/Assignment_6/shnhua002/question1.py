#Charlie Shang
#SHNHUA002
#Assignment 6 Q1

maxlen = 0
strings=['']
count=0
print("Enter strings (end with DONE):")

while strings[-1] != "DONE": #while the last item is not "DONE"
     strings.append(input())
     
     if len(strings[count]) > maxlen: #find the length of the longest word to use rjust
          maxlen = len(strings[count])
     
     count += 1 #count of the items in the list

print("\nRight-aligned list:")

for k in range(1,len(strings)-1,1):
     print(strings[k].rjust(maxlen))

