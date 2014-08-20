print("Enter strings (end with DONE):\n")#Opening statement

aligned_list=[]#List to store input
user_input=""#String to hold each input

while(user_input!="DONE"):#Loop stops when 'DONE' is entered
    user_input=input()#Input string
    aligned_list.append(user_input)#Add each input to list
    
aligned_list.remove("DONE")#Remove 'DONE' from the list
max=0#Define new variable max to store the length of the longest string inputted

#for loop to find max length
for index in aligned_list:
    if(len(index)>max):
        max=len(index)

#Print out final output
print("Right-aligned list:")

for index in aligned_list:
    print(" "*(max-len(index)),index,sep='')