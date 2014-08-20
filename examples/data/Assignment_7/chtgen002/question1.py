"""
Unique String
Genevieve Bronwyn Chetty (CHTGEN002)
02/05/2014
"""
print("Enter strings (end with DONE):")

str_input = [] #empty list
word = "" #empty string
unique_list = [] #new list

while(word!="DONE"): #loops until "DONE" is input
    word = input() 
    str_input.append(word) #word is appended to input list

str_input.remove("DONE") #remove "DONE" from list

for i in range(len(str_input)): #appends only unique strings to unique_list
    if(str_input.index(str_input[i])==i): 
        unique_list.append(str_input[i])
  
print()
print("Unique list:")

for i in range(len(unique_list)): #print unique_list
    print(unique_list[i])