"""program to count the number of votes for each political party in an election
peter m muriuki"""

#get list of party names and store them in an array
print ("Independent Electoral Commission")
print ("--------------------------------")
name_str=input("Enter the names of parties (terminated by DONE):\n"+"\n")
parties=[] 
while name_str!="DONE":
    parties.append(name_str)
    name_str=input("")#store party names in an initialised array
    
#count the frequency of each different party name and store in a counter
parties=sorted(parties)
print ("Vote counts:")
countX={}
for item in parties:
    if not item in countX:
        countX[item] = 1
    else:
        countX[item] += 1 

#print out the count of votes and respective party names in alphabetical order
for item in sorted(countX):
    a="{0:<10}".format(item)
    print (a,"-",(countX[item]))   