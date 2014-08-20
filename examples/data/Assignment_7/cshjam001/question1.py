"""Programme to remove duplicates from list
James Cushway
27-04-2014"""
string_list=[]
No_duplicates=[]
wrd=0
word_inList=input('Enter strings (end with DONE):\n')
string_list.append(word_inList)
while word_inList!='DONE':
    word_inList=input('')
    string_list.append(word_inList)
print()
string_list.remove(string_list[-1])
for i in string_list:
    if i in No_duplicates:
        continue
    else:
        No_duplicates.append(i)
    wrd=i
print('Unique list:')
for i in No_duplicates:
    print(i)
    