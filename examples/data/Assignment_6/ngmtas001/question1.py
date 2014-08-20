#Tase Ngambi
#NGMTAS001
#Question 1

names =[]
entered = ""
print("Enter strings (end with DONE):\n")

count = 0
#loops until done is entered
while entered != "DONE":
    entered = input()
    if entered != 'DONE':
        names.append(entered)
        count = count+1

print("Right-aligned list:")
lengths = []


#placing lengths of names in array

for i in range (len(names)):
    lengths.append (len(names[i]))
try:    
    #finding max length of words    
    maxSpace = int(max(lengths))
except ValueError: print()

#printing words in the required format
for x in range (len(names)):
    print (" "*(maxSpace- len(names[x])), end="")
    print(names[x])
    
