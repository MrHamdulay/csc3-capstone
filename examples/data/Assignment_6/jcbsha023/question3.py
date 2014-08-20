#program to count the number of votes in an election
#Anthony Jacob
#24 April 2014

print("Independent Electoral Commission")    #title
print("--------------------------------")
x = input("Enter the names of parties (terminated by DONE):\n")

dic = {}

while x != 'DONE':#Getting more strings from user
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
    x = input()
    
y = []
for a in dic:
    y.append(a)
y.sort()

print()
print("Vote counts:")
#producing the vote counts
for i in range(len(y)):
    k = ' '*(9-len(y[i]))
    print(y[i],k,'-',dic[y[i]])