#GLMSUM001
#Sumayah Goolam Rassool
#24 April 2014

#--------------------------------------------------print headings

print("Independent Electoral Commission")

print("--------------------------------")

#---------------------------------------------create list for all parties
parties = [] 
counters = {}

party = input("Enter the names of parties (terminated by DONE): \n") #input from user (votes)

while party != "DONE": #-----------------------reloops until user enters done
    
    parties.append(party) #--------------------adds names of parties to existing array
    
    party = input("") #-------------------------allows user to continuously enter


for item in (parties): #-------------------------creates a dictionary
    
    if not item in counters:
        
        counters[item] = 0#-----------------------sets counter=0
        
    counters[item]+=1 #--------------------------counts as per the occurence of a letter

print()#-----------------------------------------prints empty string   

#------------------------------------------------calculates and displays vote count

print("Vote counts:")

y = "{0:<10}" #---------------------------------formating output, left align

for item in sorted(counters): #-----------------display
    
    print(y.format(item),"-",counters[item])
