print("Independent Electoral Commission\n--------------------------------")

x = []


vote = input("Enter the names of parties (terminated by DONE):\n")
while vote != 'DONE':
    x.append(vote) 
    vote = input("")

counters={}


for vote in x:
    if not vote in counters:
        counters[vote]=0
    counters[vote] += 1
    sorted_parties = sorted(counters.keys())
    
    
sorted_parties = sorted(counters.keys())    
print("\n""Vote counts:")
for vote in sorted_parties:
    print(vote + ' '*(10 - len(vote)) ,'-',counters[vote])    
    
    
    
    
    