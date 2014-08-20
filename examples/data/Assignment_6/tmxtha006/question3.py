"""This program counts the number of votes for each political party and print output the formated results
Hebert Tema
21-04-2014"""

from question1 import list_str

print("Independent Electoral Commission")
print("--------------------------------")

#prompt the user to enter the parties with the sintinel "DONE"
string=input("Enter the names of parties (terminated by DONE):\n")  #string is the name of the party

string_list=list_str(string)          #function from question1.py

#use a dictionary to count number of votes for each party
dictionary={}
for i in string_list:
    if i in dictionary:
        dictionary[i]+=1
        continue
    else: dictionary[i]=1

#arrange the parties[KEYs of the dictionary]
keys=[]
for i in dictionary:
    keys.append(i)
keys.sort()

#print out the results
print()
print("Vote counts:")
for j in keys:
    print("{0:<10}".format(j),"-", dictionary[j])