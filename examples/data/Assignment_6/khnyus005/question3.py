'''
Created on 22 Apr 2014
Open fruit voting
@author: Yusuf Khan
KHNYUS005
'''
print("""Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):""")
votes = [0]#defining variables outside of loop
vote = ''
voted = []
candid8s = []

while True:#infinite loop
    vote = input()#new input
    if vote == 'DONE':
        break
    voted.append(vote)#adds vote to entire voted list
    if vote not in candid8s:
        candid8s.append(vote)#adds vote
        votes.append(0)#creates vote list of equal length

candid8s = sorted(candid8s)#alphabetically arranges candidates names
for c in range(len(candid8s)):
    votes[c] = voted.count(str(candid8s[c]))#loops through list to count votes 
    
print()
print('Vote counts:')#output
for i in range(len(candid8s)):#formatting below
    print(candid8s[i]+' '*(11-len(candid8s[i]))+'-',votes[i])