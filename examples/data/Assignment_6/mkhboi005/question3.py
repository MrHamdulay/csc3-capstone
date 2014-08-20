"""Tumi Mkhawana
22 April 2014
Assignment 6 question 3"""

print("Independent Electoral Commission")
print("--------------------------------")

parties= input("Enter the names of parties (terminated by DONE):\n")
parties_list=[]


while parties !="DONE":
    parties_list.append(parties)
    parties= input("")

diction={}
for i in parties_list:
    if not i in diction:
        diction[i]=1
    else:
        diction[i]+=1
print(' ')
print("Vote counts:")
for i in sorted(diction.keys()):
    print(i.ljust(10),"-", diction[i])


        