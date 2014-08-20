"""progaramme where a user enters a no. of strings. and they are returned with no duplicates
Sthabiso Andile Gazu
April 2014"""
#ask a user for strings
string_list=[]
string=input('Enter strings (end with DONE):\n')
while string !="DONE":
    if string in string_list:
        pass
    else:
        string_list.append(string)
    string=input('')
print()
print("Unique list:")
for strings in string_list:
    print(strings)

    

