#Program to create right-aligned list
#Joe Sutton
#23 April 2014

ans = input("Enter strings (end with DONE):\n")
list=[] #create empty list
while not ans == "DONE":
    list.append(ans)
    ans = input("")

maxlen=0 #create variable    
for i in list:
    if len(i)>maxlen:
        maxlen=len(i) #make maxlen the length of the longest name
print() #print empty row        
print("Right-aligned list:")

for j in list:
    print(" "*(maxlen-len(j)), j, sep="") #print list aligned to right