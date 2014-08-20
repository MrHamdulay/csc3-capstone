__author__ = 'JNSJOH014'
"""Input list of string and print
list without any duplicates
27/04/2014"""

str_list = []
#input strings
input_str = input("Enter strings (end with DONE):\n")
while input_str.upper()!="DONE":
    str_list.append(input_str)
    input_str = input("")
#print list with unique values
print("\nUnique list:")
temp_list = []
for item in str_list:
    if item not in temp_list:
        print(item)
        temp_list.append(item)

