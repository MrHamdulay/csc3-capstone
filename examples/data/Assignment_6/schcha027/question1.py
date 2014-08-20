#Charles Schleich SCHCHA027
#Question 1 Assignment 6

sent=""
count=0
longest=0
names_Array=[]
print("Enter strings (end with DONE):")
# while loop that fills array  until user types DONE
while sent!="DONE":
    sent=input("")
    if sent =='DONE':
        1==1
    else:
        names_Array.append(sent)
        count=count+1
        if len(sent)>longest:
           longest=len(sent)

print("\nRight-aligned list:")

length=len(names_Array)
# for loop that right aligns the inputs with the longest input
for i in range(length):
    spacecount=(longest-len(names_Array[i]))
    print(" "*spacecount,names_Array[i],sep="")
          