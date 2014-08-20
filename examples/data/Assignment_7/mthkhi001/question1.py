#MTHKHI001
#ASSIGNMENT 7
#QUESTION 1

arr = []
sentinel = ""
print("Enter strings (end with DONE):")
while sentinel != "DONE":
    sentinel = input()
    if sentinel != "DONE":
        count = 0
        for i in range (len(arr)):
            if arr[i] == sentinel:
                count = count + 1
        if count == 0:        
            arr.append(sentinel)
    
print("")

print("Unique list:")
             
for l in range (len(arr)):
    print (arr[l])
            