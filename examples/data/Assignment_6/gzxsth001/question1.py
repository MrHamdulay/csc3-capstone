"""To create a programme where a userv enter a list and it comes back right aligned
Sthabiso Andile Gazu
April 2014"""

#ask a user for a list
List=[]
list_of_strings=input('Enter strings (end with DONE):\n')
print()
x=len(list_of_strings)
while list_of_strings !="DONE":
    List.append(list_of_strings)
    list_of_strings=input('')
    if len(list_of_strings)>x:
        x=len(list_of_strings)
        #to print the list
print('Right-aligned list:')
for list_of_strings in List:
    print(" "*(x-len(list_of_strings)),list_of_strings,sep="")