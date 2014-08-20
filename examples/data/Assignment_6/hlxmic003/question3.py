# Michaela Heale
# Assignment 6 Question 3
# Voting Day

parties = []

def party_maker(name):
    s = 0
    c = 0
    while s<len(array):
        if array[s] == name:
            c+=1
        s+=1
    parties.append([name,c])
            

def display(arr):
    print()
    print("Vote counts:")
    whole = ""
    for disp in arr:
        name = disp[0]
        vote = disp[1]
        gap = 10 - len(name)
        tote = name+" "+(" "*gap)+"- "+str(vote)
        if not tote in whole:
            whole += tote + "\n"
    print(whole)
        
    
def main():
    f = 0
    while f<len(array):
        name = array[f]
        party_maker(name)
        f += 1
    parties.sort()
    display(parties)

print("Independent Electoral Commission\n--------------------------------")
opt = input("Enter the names of parties (terminated by DONE):\n")
array = []

while not opt == "DONE":
    array.append(opt)
    opt = input()

main()