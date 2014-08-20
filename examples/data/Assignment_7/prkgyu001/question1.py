#define variables.. and grid

grid = []
newgrid = []

#input data and adding in the grid
strings = input("Enter strings (end with DONE): \n")
while strings != "DONE":
    grid.append(strings)
    strings = input("")

#preventing duplicates
for i in grid:
    if not i in newgrid:
        newgrid.append(i)

#print the new list
print()
print("Unique list: ")
for i in newgrid:
    print(i)