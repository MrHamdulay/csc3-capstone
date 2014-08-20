"""programme to that erases duplicates from a list.
Karidas Tshintsholo
30-04-2014"""


List_name = []
Rama= []
ListNames = input("Enter strings (end with DONE):\n")
Names = [ListNames]


while ListNames!= "DONE":
    Names = Names+List_name
    ListNames = input("")
    List_name = [ListNames]

for i in range(len(Names)):
    if Names[i] not in Rama:
        Rama.append(Names[i])

print("\nUnique list:")
for j in Rama:
    print(j)
    
    
    
    


