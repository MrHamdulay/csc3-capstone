"""count the number of votes for each political party in an election
20/04/2014
barak setton"""
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE): ")

namelist = [] # veriables
info = 0
count =0
name= input()
while name  != "DONE":  #asking user for name
    info =0
    for i in range(len(namelist)):
        if name == (namelist[i][0]):
                info =1
                namelist[i][1] +=1 # adding count to the name
    if info !=1:
        namelist.append([name, 0])   # add the name to the list if its not in the list
     
    name = input()
  
namelist.sort() # sortng the array 
print()
print("Vote counts:")
for j in range(len(namelist)): # printing the list
    print(namelist[j][0]," "*(9-len(namelist[j][0])),"-",namelist[j][1]+1)
    