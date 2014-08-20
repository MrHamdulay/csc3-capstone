'''p rogram that takes a list of political parties and counts the number of votes for each political party
Wandile Khowa
20-04-2014
'''
def names(a): 
    ques = a
    list_n = []             #creates an empty list  
    while ques != "DONE":   #creates a sentinel "DONE" 
        list_n.append(ques) #adds word in list 'list_n'
        ques = input("")
                
    return list_n   #returns list_n to the caller

def main():
    x = "Independent Electoral Commission"
    print(x)
    print("-"*len(x))
    ans = input("Enter the names of parties (terminated by DONE): \n")
    p = sorted(names(ans))          #creates a variable to hold the returned list_n from names
    c = len(p)
    print("\nVote counts:")
    storage = []
    for i in range(c):
        if p[i] not in storage:     #checks first if p[i] is not already in the storage list
            a = p.count(p[i])
            storage.append(p[i])    #adds the name of the political party to the storage lsit    
            print(p[i].ljust(10), "-", a)
        else:
            continue
    
if __name__=='__main__':
    main()