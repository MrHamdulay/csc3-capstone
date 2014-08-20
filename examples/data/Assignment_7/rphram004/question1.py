"""programme to that erases duplicates from a list.
rama raphalalani
30-04-2014"""

#creating empty lists and also creating an input prompting the user to enter a list.
List_name = []
Rama= []
ListNames = input("Enter strings (end with DONE):\n")
Names = [ListNames]

#this loop creates a snetinel loop of when to break the loop
while ListNames!= "DONE":
    Names = Names+List_name
    ListNames = input("")
    List_name = [ListNames]
#This loop goes trhough every item in the list and checks to duplicated. duplicates do not get inserted in the second list.
for i in range(len(Names)):
    if Names[i] not in Rama:
        Rama.append(Names[i])
#printing of the new list
print("\nUnique list:")
for j in Rama:
    print(j)
    
    
    
    


