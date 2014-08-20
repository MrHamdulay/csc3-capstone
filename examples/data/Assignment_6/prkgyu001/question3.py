#define some variables
counter = {}
grid = []
newgrid = []

#collect data
print("Independent Electoral Commission \n","--------------------------------",sep = '')


names = input("Enter the names of parties (terminated by DONE): \n")
while names != "DONE":
    grid.append(names)
    names = input("")


grid.sort()
    

        
#have successfully collected necessary data




#newgrid

for i in grid:
    if not i in newgrid:
        newgrid.append(i)



# print !
print()
print("Vote counts:")
for i in newgrid:
    print(i, (10-len(i))*" " , " - " , grid.count(i), sep='')



