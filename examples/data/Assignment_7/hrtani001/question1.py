#print input list without duplicates
#Aniq Hartle
#02/05/2014

print("Enter strings (end with DONE):")

#initialise variables
str_list = []
i = str
unique = []

#take input and add to list
while i != "DONE":
    i = input()
    str_list.append(i)
#cut the last entry out (DONE)    
str_list = str_list[:len(str_list)-1]
        
print("\nUnique list:")


#If the entry does not exist in the dictionary, add it otherwise add it
for i in range(len(str_list)):
    if str_list[i] not in unique:
        unique.append(str_list[i])

#print output
for i in unique:
    print(i)