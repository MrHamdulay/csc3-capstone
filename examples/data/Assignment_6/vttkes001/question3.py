"""Poll counter
Keshin Vittee
21 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

print("Enter the names of parties (terminated by DONE):\n")

part=[]
vote = {}

while True:
    parties = input()
    if parties == "DONE":
        break
    elif parties not in part:
        part.append(parties)
        vote[parties] = 1
    else:
        vote[parties] += 1

print("Vote counts:")
part.sort()

for a in part:
    print("{0:<10} - {1}".format(a,vote[a]))
    

    
        



        