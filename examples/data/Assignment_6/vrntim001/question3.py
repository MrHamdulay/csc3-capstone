'''Vote function
Tim Mostert
23,4,14'''

print("Independent Electoral Commission")
print("-"*32)
print("Enter the names of parties (terminated by DONE):")
parties = []
while True:
    x = input()
    if x == "DONE":
        break
    parties.append(x)
    
print()
print("Vote counts:")

parties_sorted = sorted(parties)
new_list = []
for i in parties_sorted:
    if not i in new_list:
        new_list.append(i)
        print("{0:10}".format(i),"-", parties_sorted.count(i))
        
    
        
  
