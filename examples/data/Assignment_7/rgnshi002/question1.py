#Shivam Ragoonaden
#Program to enter list of strings and output them 
#28 April 2014

x = input("Enter strings (end with DONE):\n")

list = []

while x != "DONE":  #Check for sentinel
    if x not in list:
        list.append(x)  #Add item to list
    x = input("")     
    
print()
print("Unique list:")
for i in range(len(list)):   #print items of array one-by-one
    print(list[i])