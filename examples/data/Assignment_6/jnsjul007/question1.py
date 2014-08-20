#program to right-justify strings
#Julian van Rensburg
#22 April 2014
#get empty list
x=[ ]
#get string
y=input("Enter strings (end with DONE):\n")

#start counter at 0 and increment to get number of items in list
count = 0
while y !="DONE":
    x.append(y)
    y=input()
    count +=1
#max is length of logest string
    MAX=len(x[0])

for i in range (0,count):
    length = len(x[i])
    if length>MAX:
        MAX=length
print('')        
print("Right-aligned list:")            
for i in x:
    print(' '*(MAX-len(i)),i,sep='')
        