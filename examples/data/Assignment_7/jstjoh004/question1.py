# Take the unique items out of a list
# Hendrik Joosten
# 27/04/2014

# create and initialize arays
names = []
unique_names = []
x = ""

# get input from from user
x = input("Enter strings (end with DONE):\n")

while x != "DONE":
      names.append(x)
      x = input("")
      
# go through the array and append the unique items to a new array
for i in range(len(names)):
      if unique_names.count(names[i]) == 0:
            unique_names.append(names[i])

# print the new array
print("")      
print("Unique list:")
for j in range(len(unique_names)):
      print(unique_names[j])