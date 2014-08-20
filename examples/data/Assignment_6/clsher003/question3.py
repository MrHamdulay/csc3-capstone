"""program to count the votes each party gets
herman claassens
23 april 2014"""

print('Independent Electoral Commission')
print('--------------------------------')
parties_list=[]
names = input ("Enter the names of parties (terminated by DONE):\n") # get names of parties
# add names of parties to list
while names != "DONE": #sentinel to stop loop
      parties_list.append(names)
      names = input ("")


parties_dict={}
new_parties=[]
for a in parties_list:
            if a in parties_dict:        # if party name gets repeated add 1 to the votes of that party
                  parties_dict[a]+=1
            else :
                  parties_dict[a]=1
                  new_parties.append(a) # else add the party with a vote of 1
new_parties.sort() # get party names in alphabetical order
print()
print('Vote counts:')
for a in new_parties:
      print(a+' '*(10-len(a)),'-',parties_dict[a]) # print the paty names with the assocciated vote count

            
      
      
      
