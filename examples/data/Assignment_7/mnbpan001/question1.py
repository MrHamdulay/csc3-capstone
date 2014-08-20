"""Program to output a list of ordered strings
Pankaj Munbodh
28 April 2014"""

get_str=input("Enter strings (end with DONE):\n")
str_list=[]
while get_str != 'DONE':
    if not (get_str in str_list):
        str_list.append(get_str)    
    get_str=input("")
    
#Output
print()
print("Unique list:")
for i in str_list:
    print(i)