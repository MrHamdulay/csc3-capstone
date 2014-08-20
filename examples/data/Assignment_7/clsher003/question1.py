"""print list of strings without duplicates
herman claassens
27 april 2014"""

strings=[]
string=input('Enter strings (end with DONE):\n')  # create the list of strings containing duplicates
while string!='DONE':
    strings.append(string)
    string=input("")

def deduplicate(original_list):
    deduplicated_list = [] # if strings is in original list but not in the new list, add to the new list
    for x in original_list: # if strings is in new list, do not add again
        if x not in deduplicated_list:
            deduplicated_list.append(x)
    return deduplicated_list

new_list=deduplicate(strings) # print out characters in this new list
print()
print('Unique list:')
for a in new_list:
    print(a)