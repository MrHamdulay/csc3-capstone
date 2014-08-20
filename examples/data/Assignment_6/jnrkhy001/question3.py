#Khyati Jinerdeb
#Assignment 6
#25 April 2014
#program to count the number of votes for each political party in an election

print("Independent Electoral Commission")  
print("--------------------------------")

parties=[]

name=input("Enter the names of parties (terminated by DONE):\n")  #prompt user to enter names of parties

dict={}    #defines a dictionnary

while True:
    parties.append(name)   #to add subsequent names in the list
    
    if name=="DONE":
        break             #using break statement to stop running the program
    elif name not in dict:
        dict[name]=1      
    else:
        dict[name]+=1     #if the name entered appears more than once, increase the count that is add 1
    name=input()
    
        
parties=dict.keys()
parties=sorted(parties)   #these 2 functions are basically to sort the list of parties in alphabetical order



print("\nVote counts:")   
for i in parties:
    print(i.ljust(10),"-",dict[i])   #to left justify the names of parties by using a width of 10
    






    
    
    
    

    
    