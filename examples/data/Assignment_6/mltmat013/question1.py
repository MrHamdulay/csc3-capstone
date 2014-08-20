''' Program to right-align a list of strings
21 April 2014
Matshepo Malatji '''

List = []
#Allow user to input strings
sListItem = input("Enter strings (end with DONE):\n")

while not sListItem.upper() == 'DONE':
#Store in a list
    List.append(sListItem)
    sListItem = input('')
print()

print('Right-aligned list:')
if len(List) > 0:
    largest = len(List[0])
    #Determine the longest string
    for i in range(1,len(List)):
        if len(List[i]) > largest:
            largest = len(List[i])
        
#Align to the right
    
    string ='{0:>' + str(largest) +'}'
    for k in range(len(List)):
        print(string.format(List[k]))