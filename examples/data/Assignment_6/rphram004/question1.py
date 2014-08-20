"""programme to align inout strings to the right
rama raphalalani
22-04-2014"""

#Getting an input of strings and making a list with those strings
ListNames = []
List = (input('Enter strings (end with DONE):\n'))
Length = len(List)
ListNames = []

#creating the sentinel loop with DONE
if List != 'DONE':
    ListNames.append(List)

#continuiting with the sentinel loop and also getting the length of the strings
while List != 'DONE':
    List = input()
    Length2 = len(List)
    if Length2 > Length:
        Length = Length2
    if List != 'DONE':
        ListNames.append(List)
print()

#creating the condition for the alignment of the strings to the right        
Align=(len(ListNames))
Initial = 0
print('Right-aligned list:')
while Initial < Align:
    print(ListNames[Initial].rjust(Length))
    Initial = Initial + 1
    