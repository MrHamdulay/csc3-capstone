""" Luveshen Pillay
25/4/2014
Print unique items of a list"""

# Variables to be used in functions

listinput=[]
unique=[]
string=""

# Population of list string
while string != "DONE":
    if listinput== []:
        print("Enter strings (end with DONE):\n")
        string=input("")
        if string != "DONE":
            listinput.append(string)

    else:
       
            string=input("")
            if string != "DONE":
                listinput.append(string)
                

# Processing of list               
[unique.append(item) for item in listinput if item not in unique]
            
# Print list            
print("Unique list:",end="\n")
for i in unique:
    print(i)
    



        