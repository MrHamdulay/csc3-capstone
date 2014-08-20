'''Sanele Mdlalose
MDLSAN019
A Program that alignes list of strings on their right
Assignment6,question1
22 April 2014'''

# create prompt for the user to enter strings
strings = input("Enter strings (end with DONE):\n")
new_list = []   #create an empty list
if strings!='DONE':
    while True:   
        new_list.append(strings)   #Append each string into new_list
        strings = input("")   #Prompt for more input(strings)
        if strings == "DONE":
            print()
            break
    
else:
    print()
        
print("Right-aligned list:")
track = []   #create an empty list  
for i in range (len(new_list)): 
    track.append(len(new_list[i]))   #Append the length of each item into track
    
if track!=[]:
    maximum=max(track)  #Find the maximum length  
    for j in range (len(new_list)):
        print(new_list[j].rjust(maximum))   #Output a right justified output, with the width of the maximum number.

    
        
    
    

    