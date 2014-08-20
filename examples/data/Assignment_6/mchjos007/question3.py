#code to enter in votes for different politcal parties that then prints each party and the votes they have recieved#
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
partys = []
userSaysWhat = input("")
if not userSaysWhat =="DONE":
        while userSaysWhat != "DONE":
                partys.append(userSaysWhat)
                userSaysWhat = input("")
        partys.sort()
        print("")
        print("Vote counts:")
        while partys[0] != partys[(len(partys))-1]:
                print(partys[0] + (" "*(10-len(partys[0]))) + " - " + str(partys.count(partys[0])))
                temp = partys[0]
                while temp == partys[0]:
                        partys.remove(temp)
        print(partys[0] + (" "*(10-len(partys[0]))) + " - " + str(partys.count(partys[0])))
else:
        print("")
        print("Vote counts:")