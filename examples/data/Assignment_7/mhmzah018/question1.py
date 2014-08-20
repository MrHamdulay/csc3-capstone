"""Assignment 7- question 1
Zaheer Mahmood
27-04-2014"""

storage = []
answer=input("Enter strings (end with DONE):\n")
storage.append(answer)
#construct loop to allow for inputs
while answer != "DONE":
    answer = input("")
    storage.append(answer)
storage.remove("DONE")
    
#construct loop to get unique list
new_storage = []
new_answer = ""
for i in storage:
    new_answer == i
    if i in new_storage:
        continue
    else:
        new_storage.append(i)
        
print()
print("Unique list:")
for n in range(len(new_storage)):
    print(new_storage[n])