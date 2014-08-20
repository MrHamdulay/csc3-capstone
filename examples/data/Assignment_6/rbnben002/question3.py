print("Independent Electoral Commission")
print("--------------------------------")
def Begin():

    user = input("Enter the names of parties (terminated by DONE):\n")
    parties = []
    while user != "DONE":
        parties.append(user)
        user = input()
    print("")
    print("Vote counts:")
    Voting(parties)

def Voting(parties):
    parties.sort()
    count = 1
    for i in range(0,len(parties)-1):
        if parties[i] == parties[i+1]:
            count+=1
            if i == len(parties)-2:
                print(parties[i]+ " " * spaces + "- ",count,sep = "")
        else:
            spaces = 10 - (len(parties[i])-1)
            print(parties[i]+ " " * spaces + "- ",count,sep = "")
            count = 1 
            if i == len(parties)-2:
                spaces = 10 - (len(parties[i+1])-1)
                print(parties[i+1]+ " " * spaces + "- ",count,sep = "")  
Begin()