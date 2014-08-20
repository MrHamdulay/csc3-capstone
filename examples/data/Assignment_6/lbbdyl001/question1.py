"""
Aligning List of String to the Right
"""
print("Enter strings (end with DONE):") #input

str_list = [] #empty list
str_input = "" #empty string

while(str_input!="DONE"): #loop ends when str_input = "DONE"
    str_input=input() 
    str_list.append(str_input) #input is appended to the list

str_list.remove("DONE") #"DONE" is removed from list 

max_length = 0   

for i in str_list: #max length found using for loop 
    if(len(i)>max_length): 
        max_length=len(i)
print()
print("Right-aligned list:")

for i in str_list:
    print(" "*(max_length-len(i)),i,sep='') #max_length minus length is number of spaces