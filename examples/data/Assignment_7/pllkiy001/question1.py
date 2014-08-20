#program to print a list in the same order without duplicates
#kiyarah pillay
#30 april 2014

#get strings from user
string_list=input("Enter strings (end with DONE):\n")
string=[]
#done is sentinel value
while string_list != "DONE":
#turns strings into a list 
    string.append(string_list)
    string_list=input("")
print_list=[]
for i in string:
    if i in print_list:
        continue
    else:
        print_list.append(i)
        
print()
print("Unique list:")
#prints the words in a list instead of side by side
for a in print_list:
    print (a)
    

        
    
            
            
            

        